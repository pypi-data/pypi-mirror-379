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


# distributed script to prealign fMOST images to given template
import argparse
from typing import List
import os
import logging
logging.basicConfig()
from glob import glob
import numpy as np

import torch
from torch import distributed as dist

import hydra
from omegaconf import DictConfig, OmegaConf
from torch.nn import functional as F
from tqdm import tqdm
from fireants.io.image import Image, BatchedImages
from fireants.registration import AffineRegistration
from fireants.scripts.template.template_helpers import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def setup_distributed(local_rank, world_size):
    '''
    Setup distributed training
    '''
    global logger
    logger.info(f'Setting up distributed training with local rank {local_rank} and world size {world_size}.')
    dist.init_process_group(backend='nccl')

def dist_cleanup(world_size):
    ''' cleanup distributed training '''
    global logger
    logger.info('Cleaning up distributed training')
    dist.destroy_process_group()

def main(args):
    # get distributed setup  
    local_rank = int(os.environ.get('LOCAL_RANK', 0))
    world_size = int(os.environ.get('WORLD_SIZE', 1))
    logger = logging.getLogger(__name__ + f"_{local_rank}")
    logger.setLevel(logging.INFO)

    # setup distributed training
    setup_distributed(local_rank, world_size)
    torch.cuda.set_device(local_rank)
    device = torch.cuda.current_device()
    files = sorted(list(glob(args.images_glob)))
    files = [file for file in files if args.images_neg_glob not in file]


    print(f"Found {len(files)} files to prealign.")
    files = files[local_rank::world_size]

    template_img = Image.load_file(args.template_path, orientation=args.orientation, device=device)
    template_img.array.div_(255.0)
    template_batch = BatchedImages(template_img)

    # run affine for each image
    for file in tqdm(files, desc="Prealigning images"):
        outpath = file.replace(args.replace_from, args.replace_to)
        if os.path.exists(outpath):
            print(f"{outpath} exists already.")
            continue

        if file == args.template_path:
            # create a symlink
            if not os.path.exists(outpath):
                os.symlink(file, outpath)
            else:
                print(f"Symlink {outpath} already exists.")
            continue
        logger.info(f"Prealigning image {file} to template {args.template_path}.")
        # else register image to template
        moving_img = Image.load_file(file, orientation=args.orientation, device=device)
        moving_img.array.div_(255.0)
        moving_batch = BatchedImages(moving_img)
        reg = AffineRegistration(scales=[4, 2, 1], iterations=[300, 200, 50], fixed_images=template_batch, moving_images=moving_batch, loss_type='cc', optimizer='Adam', optimizer_lr=3e-3)
        reg.optimize(False)
        # get moved image
        moved_img = reg.evaluate(template_batch, moving_batch)
        moved_img = (moved_img[0, 0].detach().cpu().numpy() * 255.0).astype(np.uint8)
        # simple loop to avoid race condition for writing (sitk.WriteImage is not thread safe)
        for i in range(world_size):
            if i == local_rank:
                moved_img = sitk.GetImageFromArray(moved_img)
                moved_img.CopyInformation(template_img.itk_image)
                sitk.WriteImage(moved_img, outpath)
                print(f"Saved moved image {outpath}.")
            dist.barrier()

    dist_cleanup(world_size)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--template_path", type=str, required=True)
    parser.add_argument("--images_glob", type=str, required=True)
    parser.add_argument("--images_neg_glob", type=str, default="aligned_to")
    parser.add_argument("--replace_from", type=str, required=True)
    parser.add_argument("--replace_to", type=str, required=True)
    parser.add_argument("--orientation", type=str, default='SLA')
    args = parser.parse_args()
    main(args)
