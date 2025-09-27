import pytest
import torch
import SimpleITK as sitk
import numpy as np
import os
import subprocess
import logging
from pathlib import Path
import torch.nn.functional as F

from fireants.registration.greedy import GreedyRegistration
from fireants.registration.syn import SyNRegistration
from fireants.io.image import Image, BatchedImages
from fireants.utils.imageutils import jacobian
try:
    from .conftest import dice_loss
except ImportError:
    from conftest import dice_loss

# Set up logging
logger = logging.getLogger(__name__)

test_data_dir = Path(__file__).parent / "test_data"
fixed_image_path = str(test_data_dir / "deformable_image_1.nii.gz")
moving_image_path = str(test_data_dir / "deformable_image_2.nii.gz")
fixed_seg_path = str(test_data_dir / "deformable_seg_1.nii.gz")
moving_seg_path = str(test_data_dir / "deformable_seg_2.nii.gz")

@pytest.fixture(scope="class")
def greedy_registration_results():
    """Fixture to compute and share greedy registration results across subtests."""
    # Create output directory
    output_dir = Path(__file__).parent / "test_results"
    output_dir.mkdir(exist_ok=True)
    ext = "nii.gz"

    fixed_image = Image.load_file(fixed_image_path)
    moving_image = Image.load_file(moving_image_path)
    fixed_seg = Image.load_file(fixed_seg_path, is_segmentation=True)
    moving_seg = Image.load_file(moving_seg_path, is_segmentation=True)

    # Create BatchedImages objects
    fixed_batch = BatchedImages([fixed_image])
    moving_batch = BatchedImages([moving_image])
    moving_seg_batch = BatchedImages([moving_seg])
    fixed_seg_batch = BatchedImages([fixed_seg])
    
    # Run greedy registration
    reg = GreedyRegistration(
        scales=[4, 2, 1],
        iterations=[200, 100, 50],
        fixed_images=fixed_batch,
        moving_images=moving_batch,
        loss_type='cc',
        optimizer='Adam',
        # optimizer_lr=0.5,
        # smooth_grad_sigma=1.0,
        # smooth_warp_sigma=0.5,
        optimizer_lr=0.2,
        smooth_warp_sigma=0.25,
        smooth_grad_sigma=0.5
    )
    
    # Optimize the registration
    reg.optimize()
    
    # Get results
    moved_seg_batch = reg.evaluate(fixed_seg_batch, moving_seg_batch).detach()
    moved_image = reg.evaluate(fixed_batch, moving_batch).detach()
   
    # Save results
    reg.save_moved_images(moved_image, str(output_dir / "moved_image_greedy.nii.gz"))
    reg.save_moved_images(moved_seg_batch, str(output_dir / "moved_seg_greedy.nii.gz"))
    
    # Save transformation field
    reg.save_as_ants_transforms(str(output_dir / f"warp_field_greedy.{ext}"))

    return {
        'reg': reg,
        'fixed_batch': fixed_batch,
        'moving_batch': moving_batch,
        'fixed_seg_batch': fixed_seg_batch,
        'moving_seg_batch': moving_seg_batch,
        'moved_seg_batch': moved_seg_batch,
        'moved_image': moved_image,
        'output_dir': output_dir,
        'fixed_path': fixed_image_path,
        'moving_path': moving_image_path,
        'transform_path': str(output_dir / f"warp_field_greedy.{ext}"),
    }

class TestGreedyRegistration:
    """Test suite for greedy deformable registration."""
    
    def test_initial_dice_score(self, greedy_registration_results):
        """Test that initial Dice score is close to 0."""
        dice_score_before = 1 - dice_loss(greedy_registration_results['moving_seg_batch'](), 
                                        greedy_registration_results['fixed_seg_batch'](), 
                                        reduce=False).mean(0)
        mean_dice = dice_score_before.mean()
        logger.info(f"Dice score before registration: {mean_dice:.3f}")
        assert mean_dice < 0.6, f"Initial Dice score ({mean_dice:.3f}) should be small"
    
    def test_final_dice_score(self, greedy_registration_results):
        """Test that final Dice score is above threshold."""
        dice_scores = 1 - dice_loss(greedy_registration_results['moved_seg_batch'], 
                                  greedy_registration_results['fixed_seg_batch'](), 
                                  reduce=False).mean(0)
        mean_dice = dice_scores.mean()
        logger.info(f"Average Dice score: {mean_dice:.3f}")
        assert mean_dice > 0.75, f"Average Dice score ({mean_dice:.3f}) is below threshold"
        
        # Log detailed results
        logger.info("\nGreedy Registration Results:")
        logger.info(f"Average Dice Score: {mean_dice:.3f}")
        logger.info(f"Number of labels with Dice > 0.7: {sum(1 for d in dice_scores if d > 0.7)}")
        logger.info(f"Number of labels with Dice > 0.8: {sum(1 for d in dice_scores if d > 0.8)}")
        logger.info(f"Number of labels with Dice > 0.9: {sum(1 for d in dice_scores if d > 0.9)}")
    
    def test_transform_consistency(self, greedy_registration_results):
        """Test that saved transform and antsApplyTransforms give consistent results."""
        # Apply transform using antsApplyTransforms
        fixed_path = greedy_registration_results['fixed_path']
        moving_path = greedy_registration_results['moving_path']
        transform_path = greedy_registration_results['transform_path']
        ants_output = str(greedy_registration_results['output_dir'] / "moved_image_ants_greedy.nii.gz")
        
        # Run antsApplyTransforms with the ANTs transform field
        cmd = f"antsApplyTransforms -d 3 -i {moving_path} -r {fixed_path} -t {transform_path} -o {ants_output}"
        subprocess.run(cmd, shell=True, check=True)
        
        # Load and compare results
        ants_result = Image.load_file(ants_output)
        ants_array = ants_result.array.squeeze().cpu().numpy()
        moved_array = greedy_registration_results['moved_image'].squeeze().cpu().numpy()
        logger.info(f"ANTS array min: {ants_array.min()}, max: {ants_array.max()}")
        logger.info(f"Moved array min: {moved_array.min()}, max: {moved_array.max()}")
        
        # Compare using relative error
        rel_error = np.mean(np.abs(ants_array - moved_array) / (np.abs(moved_array) + 1e-6))
        logger.info(f"Relative error: {rel_error:.4f}")
        assert rel_error < 0.005, f"Transform consistency check failed. Relative error: {rel_error:.4f}"

    def test_jacobian_determinant(self, greedy_registration_results):
        """Test that the transformation has positive Jacobian determinant everywhere."""
        reg = greedy_registration_results['reg']
        fixed_batch = greedy_registration_results['fixed_batch']
        moving_batch = greedy_registration_results['moving_batch']
        
        # Get the warped coordinates
        coords = reg.get_warped_coordinates(fixed_batch, moving_batch)
        
        # Compute Jacobian determinant using imageutils.jacobian
        J = jacobian(coords, normalize=True).permute(0, 2, 3, 4, 1, 5)[:, 1:-1, 1:-1, 1:-1, :]
        
        # Compute determinant
        det = torch.linalg.det(J)
        
        # Check for negative determinants
        neg_det = (det < 0).float().mean()
        logger.info(f"Percentage of negative Jacobian determinants: {neg_det:.4f}")
        
        # Assert that there are no negative determinants
        assert neg_det < 0.0001, f"Found {neg_det:.4f}% negative Jacobian determinants"

    def test_warp_inverse_composition(self, greedy_registration_results):
        """
        Test that the composition of warp and inverse warp gives identity transformation.
        Note that the error is not actually relative error, but the error relative to the discretization of the grid.
        
        """

        reg = greedy_registration_results['reg']
        fixed_batch = greedy_registration_results['fixed_batch']
        moving_batch = greedy_registration_results['moving_batch']
        
        # Get forward and inverse warps
        warp = reg.get_warped_coordinates(fixed_batch, moving_batch)
        inv_warp = reg.get_inverse_warped_coordinates(fixed_batch, moving_batch)
        
        # Create identity grid
        grid = F.affine_grid(torch.eye(3, 4, device=warp.device)[None], 
                           [1, 1] + list(warp.shape[1:-1]), 
                           align_corners=True)
        
        # Compose warp and inverse warp
        composed = F.grid_sample((warp - grid).permute(0, 4, 1, 2, 3), 
                               inv_warp, 
                               mode='bilinear', 
                               align_corners=True).permute(0, 2, 3, 4, 1) + inv_warp
        
        # Compute relative error
        H, W, D = warp.shape[1:-1]
        loss = (composed - grid)
        loss[..., 0] *= (W-1)/2
        loss[..., 1] *= (H-1)/2
        loss[..., 2] *= (D-1)/2
        rel_error = (loss**2).mean()
        
        logger.info(f"Relative error in warp-inverse composition: {rel_error:.6f}")
        assert rel_error < 0.001, f"Warp-inverse composition error ({rel_error:.6f}) exceeds threshold"
        
        # Also check inverse-warp composition
        composed_inv = F.grid_sample((inv_warp - grid).permute(0, 4, 1, 2, 3), 
                                   warp, 
                                   mode='bilinear', 
                                   align_corners=True).permute(0, 2, 3, 4, 1) + warp
        
        loss_inv = (composed_inv - grid)
        loss_inv[..., 0] *= (W-1)/2
        loss_inv[..., 1] *= (H-1)/2
        loss_inv[..., 2] *= (D-1)/2
        rel_error_inv = (loss_inv**2).mean()
        
        logger.info(f"Relative error in inverse-warp composition: {rel_error_inv:.6f}")
        assert rel_error_inv < 0.001, f"Inverse-warp composition error ({rel_error_inv:.6f}) exceeds threshold"


@pytest.fixture(scope="class")
def syn_registration_results():
    """Fixture to compute and share SyN registration results across subtests."""
    # Create output directory
    output_dir = Path(__file__).parent / "test_results"
    output_dir.mkdir(exist_ok=True)
    ext = "nii.gz"

    fixed_image = Image.load_file(fixed_image_path)
    moving_image = Image.load_file(moving_image_path)
    fixed_seg = Image.load_file(fixed_seg_path, is_segmentation=True)
    moving_seg = Image.load_file(moving_seg_path, is_segmentation=True)

    # Create BatchedImages objects
    fixed_batch = BatchedImages([fixed_image])
    moving_batch = BatchedImages([moving_image])
    moving_seg_batch = BatchedImages([moving_seg])
    fixed_seg_batch = BatchedImages([fixed_seg])
    
    # Run SyN registration
    reg = SyNRegistration(
        scales=[4, 2, 1],
        iterations=[200, 100, 50],
        fixed_images=fixed_batch,
        moving_images=moving_batch,
        loss_type='cc',
        optimizer='Adam',
        optimizer_lr=0.2,
        smooth_warp_sigma=0.25,
        smooth_grad_sigma=0.5
    )
    
    # Optimize the registration
    reg.optimize()
    
    # Get results
    moved_seg_batch = reg.evaluate(fixed_seg_batch, moving_seg_batch).detach()
    moved_image = reg.evaluate(fixed_batch, moving_batch).detach()
   
    # Save results
    reg.save_moved_images(moved_image, str(output_dir / "moved_image_syn.nii.gz"))
    reg.save_moved_images(moved_seg_batch, str(output_dir / "moved_seg_syn.nii.gz"))
    
    # Save transformation field
    reg.save_as_ants_transforms(str(output_dir / f"warp_field_syn.{ext}"))

    return {
        'reg': reg,
        'fixed_batch': fixed_batch,
        'moving_batch': moving_batch,
        'fixed_seg_batch': fixed_seg_batch,
        'moving_seg_batch': moving_seg_batch,
        'moved_seg_batch': moved_seg_batch,
        'moved_image': moved_image,
        'output_dir': output_dir,
        'fixed_path': fixed_image_path,
        'moving_path': moving_image_path,
        'transform_path': str(output_dir / f"warp_field_syn.{ext}"),
    }

class TestSyNRegistration:
    """Test suite for SyN deformable registration."""
    
    def test_initial_dice_score(self, syn_registration_results):
        """Test that initial Dice score is close to 0."""
        dice_score_before = 1 - dice_loss(syn_registration_results['moving_seg_batch'](), 
                                        syn_registration_results['fixed_seg_batch'](), 
                                        reduce=False).mean(0)
        mean_dice = dice_score_before.mean()
        logger.info(f"Dice score before registration: {mean_dice:.3f}")
        assert mean_dice < 0.6, f"Initial Dice score ({mean_dice:.3f}) should be small"
    
    def test_final_dice_score(self, syn_registration_results):
        """Test that final Dice score is above threshold."""
        dice_scores = 1 - dice_loss(syn_registration_results['moved_seg_batch'], 
                                  syn_registration_results['fixed_seg_batch'](), 
                                  reduce=False).mean(0)
        mean_dice = dice_scores.mean()
        logger.info(f"Average Dice score: {mean_dice:.3f}")
        assert mean_dice > 0.75, f"Average Dice score ({mean_dice:.3f}) is below threshold"
        
        # Log detailed results
        logger.info("\nSyN Registration Results:")
        logger.info(f"Average Dice Score: {mean_dice:.3f}")
        logger.info(f"Number of labels with Dice > 0.7: {sum(1 for d in dice_scores if d > 0.7)}")
        logger.info(f"Number of labels with Dice > 0.8: {sum(1 for d in dice_scores if d > 0.8)}")
        logger.info(f"Number of labels with Dice > 0.9: {sum(1 for d in dice_scores if d > 0.9)}")
    
    def test_transform_consistency(self, syn_registration_results):
        """Test that saved transform and antsApplyTransforms give consistent results."""
        # Apply transform using antsApplyTransforms
        fixed_path = syn_registration_results['fixed_path']
        moving_path = syn_registration_results['moving_path']
        transform_path = syn_registration_results['transform_path']
        ants_output = str(syn_registration_results['output_dir'] / "moved_image_ants_syn.nii.gz")
        
        # Run antsApplyTransforms with the ANTs transform field
        cmd = f"antsApplyTransforms -d 3 -i {moving_path} -r {fixed_path} -t {transform_path} -o {ants_output}"
        subprocess.run(cmd, shell=True, check=True)
        
        # Load and compare results
        ants_result = Image.load_file(ants_output)
        ants_array = ants_result.array.squeeze().cpu().numpy()
        moved_array = syn_registration_results['moved_image'].squeeze().cpu().numpy()
        logger.info(f"ANTS array min: {ants_array.min()}, max: {ants_array.max()}")
        logger.info(f"Moved array min: {moved_array.min()}, max: {moved_array.max()}")
        
        # Compare using relative error
        rel_error = np.mean(np.abs(ants_array - moved_array) / (np.abs(moved_array) + 1e-6))
        logger.info(f"Relative error: {rel_error:.4f}")
        assert rel_error < 0.005, f"Transform consistency check failed. Relative error: {rel_error:.4f}"

    def test_jacobian_determinant(self, syn_registration_results):
        """Test that the transformation has positive Jacobian determinant everywhere."""
        reg = syn_registration_results['reg']
        fixed_batch = syn_registration_results['fixed_batch']
        moving_batch = syn_registration_results['moving_batch']
        
        # Get the warped coordinates
        coords = reg.get_warped_coordinates(fixed_batch, moving_batch)
        
        # Compute Jacobian determinant using imageutils.jacobian
        J = jacobian(coords, normalize=True).permute(0, 2, 3, 4, 1, 5)[:, 1:-1, 1:-1, 1:-1, :]
        
        # Compute determinant
        det = torch.linalg.det(J)
        
        # Check for negative determinants
        neg_det = (det < 0).float().mean()
        logger.info(f"Percentage of negative Jacobian determinants: {neg_det:.4f}")
        
        # Assert that there are no negative determinants
        assert neg_det < 0.0001, f"Found {neg_det:.4f}% negative Jacobian determinants" 