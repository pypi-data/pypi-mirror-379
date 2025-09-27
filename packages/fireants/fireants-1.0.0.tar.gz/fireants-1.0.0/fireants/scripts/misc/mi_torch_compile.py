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


import torch
import time
import numpy as np

def parzen_window(image1, image2, num_bins=32):
    # image: [B, N]
    batch_size = image1.shape[0]
    image1 = torch.clamp(image1, 0, 1).reshape(batch_size, -1, 1)
    image2 = torch.clamp(image2, 0, 1).reshape(batch_size, -1, 1)   # [B, N, 1]
    bin_centers = torch.linspace(0, 1, num_bins).reshape(1, 1, -1).to(image1)  # [1, 1, num_bins]
    bin_width = torch.mean(bin_centers[1:] - bin_centers[:-1])
    sigma = bin_width / 2

    weight1 = torch.exp(
        -(image1 - bin_centers) ** 2 / (2 * sigma ** 2)  # [B, N, num_bins]
    )  # (batch, num_sample, num_bin)
    weight1 = weight1 / torch.sum(weight1, dim=-1, keepdim=True)  # (batch, num_sample, num_bin)
    pa = torch.mean(weight1, dim=-2, keepdim=True)  # (batch, 1, num_bin)

    weight2 = torch.exp(
        -(image2 - bin_centers) ** 2 / (2 * sigma ** 2)  # [B, N, num_bins]
    )  # (batch, num_sample, num_bin)
    weight2 = weight2 / torch.sum(weight2, dim=-1, keepdim=True)  # (batch, num_sample, num_bin)
    pb = torch.mean(weight2, dim=-2, keepdim=True)  # (batch, 1, num_bin)

    pab = torch.bmm(weight1.permute(0, 2, 1), weight2.to(weight1))
    papb = torch.bmm(pa.permute(0, 2, 1), pb.to(pa))
    return pab, papb



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_bins", type=int, default=32)
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--num_sample", type=int, default=192 * 160 * 224)
    parser.add_argument("--use_compile", action="store_true")
    parser.add_argument("--num_warmup", type=int, default=2)
    args = parser.parse_args()

    # get images
    img1 = torch.rand(args.batch_size, args.num_sample).cuda()
    img2 = torch.rand(args.batch_size, args.num_sample).cuda().requires_grad_(True)
    if args.use_compile:
        parzen_window = torch.compile(parzen_window)
        print("Compiled parzen window")
    else:
        print("Not compiled parzen window")
    # warmup
    for _ in range(args.num_warmup):
        _, _ = parzen_window(img1+np.random.randn(), img2+np.random.randn(), args.num_bins)
    del _

    mem = torch.cuda.memory_allocated()

    start = time.perf_counter()
    pab, papb = parzen_window(img1, img2, args.num_bins)
    torch.cuda.synchronize()
    end = time.perf_counter()
    print(f"Time: {end - start}s")
    print(f"Memory: {(torch.cuda.memory_allocated() - mem) / 1024 / 1024} MB")
