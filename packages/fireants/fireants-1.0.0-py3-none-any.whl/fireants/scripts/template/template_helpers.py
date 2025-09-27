# Copyright (c) 2025 Rohit Jena. All rights reserved.
# 
# This file is part of FireANTs, distributed under the terms of
# the FireANTs License version 1.0. A copy of the license can be found
# in the LICENSE file at the root of this repository.
#
# IMPORTANT: This code is part of FireANTs and its use, reproduction, or
# distribution must comply with the full license terms, including:
# - Maintaining all copyright notices and bibliography references
# - Using only approved (re)-distribution channels 
# - Proper attribution in derivative works
#
# For full license details, see: https://github.com/rohitrango/FireANTs/blob/main/LICENSE 


''' author: rohitrango

helper functions for the template building script
'''

import time
import os
import torch
from fireants.io.image import Image, BatchedImages
import SimpleITK as sitk

class Timer:
    def __init__(self, description: str, logger):
        self.description = description
        self.logger = logger

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        if self.logger is not None:
            self.logger.info(f'"{self.description}" took {elapsed_time:.2f} seconds.')

def check_args(args, logger):
    ''' 
    Parameters:
    args: argparse.Namespace
        arguments passed to the script
    logger: logging.Logger
    '''
    # save tmpdir
    if args.tmpdir is None:
        args.tmpdir = os.environ.get('TMPDIR', '/tmp')
    
    # check for last registration 
    if args.do_deform:
        args.last_reg = 'deform'
    elif args.do_affine:
        args.last_reg = 'affine'
    elif args.do_rigid:
        args.last_reg = 'rigid'
    elif args.do_moments:
        args.last_reg = 'moments'
    else:
        logger.error('No registration type specified')
        return False

    return True

def get_image_files(image_file, image_prefix=None, image_suffix=None, num_subjects=None):
    ''' get image files and process them '''
    with open(image_file, 'r') as f:
        image_files = f.readlines()
    image_files = list(filter(lambda x: len(x) > 0, [f.strip() for f in image_files]))
    if image_prefix is not None:
        image_files = [image_prefix + f for f in image_files]
    if image_suffix is not None:
        image_files = [f + image_suffix for f in image_files]
    if num_subjects is not None:
        image_files = image_files[:num_subjects]
    return image_files

def save_moved(moved_tensor, id_list, save_dir, template_img, prefix=None):
    '''
    save the moved images

    A very bad way to create a lock
    '''
    world_size = torch.distributed.get_world_size()
    local_rank = torch.distributed.get_rank()
    # poll among all ranks
    for lockid in range(world_size):
        if lockid == local_rank:
            # run the save function
            for moved, id in zip(moved_tensor, id_list):
                movedimg = moved[0].detach().cpu().numpy()
                savename = f"{prefix}_{id}" if prefix is not None else id
                # create itk object
                img = sitk.GetImageFromArray(movedimg)
                img.CopyInformation(template_img.itk_image)
                sitk.WriteImage(img, f"{save_dir}/{savename}.nii.gz")
                print(f"Saved moved image {savename}.")
            torch.distributed.barrier()
        else:
            torch.distributed.barrier()
         
        

def save_additional(reg_obj, init_template_batch, additional_save_batches, batchid, save_dir):
    ''' save additional files 
    
    reg_obj: registration object
    init_template_batch: BatchedImages of a single image containing template
    additional_save_batches: list of tuples containing additional files to save
    batchid: int (which batch to save right now) - the reg_obj is run for that batchid
    save_dir: str (directory to save the files)
    '''
    for add_id, (add_filebatches, add_idbatches, is_segm) in enumerate(additional_save_batches):
        add_files = add_filebatches[batchid]
        add_ids = add_idbatches[batchid]
        moving_batch = BatchedImages([Image.load_file(imgfile, device=torch.cuda.current_device(), is_segmentation=is_segm) for imgfile in add_files])
        moved_images = reg_obj.evaluate(init_template_batch, moving_batch)
        save_moved(moved_images, add_ids, save_dir, init_template_batch.images[0], f"add_{add_id}")