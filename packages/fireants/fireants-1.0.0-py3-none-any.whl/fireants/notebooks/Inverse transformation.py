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


#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from fireants.io import Image, BatchedImages
from fireants.registration import GreedyRegistration
import torch
from torch import nn
from torch.nn import functional as F
get_ipython().run_line_magic('pylab', '')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


image1 = Image.load_file("/mnt/rohit_data2/neurite-OASIS/OASIS_OAS1_0003_MR1/slice_norm_2d.nii.gz")
image1label =  Image.load_file("/mnt/rohit_data2/neurite-OASIS/OASIS_OAS1_0003_MR1/slice_seg4_2d.nii.gz")

image2 = Image.load_file("/mnt/rohit_data2/neurite-OASIS/OASIS_OAS1_0005_MR1/slice_norm_2d.nii.gz")
image2label =  Image.load_file("/mnt/rohit_data2/neurite-OASIS/OASIS_OAS1_0005_MR1/slice_seg4_2d.nii.gz")


# In[3]:


image1, image2 = BatchedImages(image1), BatchedImages(image2)


# In[4]:


reg = GreedyRegistration(scales=[4, 2, 1], iterations=[200, 100, 50],
                         fixed_images=image1, 
                         moving_images=image2)


# In[5]:


reg.optimize()


# In[6]:


moved = reg.evaluate(image1, image2)


# In[7]:


fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(image2()[0,0].detach().cpu(),'gray'); axs[0].set_title("Moving")
axs[1].imshow(image1()[0,0].detach().cpu(),'gray'); axs[1].set_title("Fixed")
axs[2].imshow(moved[0,0].detach().cpu(),'gray'); axs[2].set_title("Moving to Fixed")


# In[50]:


fixed2moving = reg.evaluate_inverse(image1, image2, smooth_warp_sigma=0.25, smooth_grad_sigma=0.5)


# In[51]:


fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(image1()[0,0].detach().cpu(),'gray'); axs[0].set_title("Fixed")
axs[1].imshow(image2()[0,0].detach().cpu(),'gray'); axs[1].set_title("Moving")
axs[2].imshow(fixed2moving[0,0].detach().cpu(),'gray'); axs[2].set_title("Fixed to moving")


# In[52]:


warp = reg.get_warped_coordinates(image1, image2)


# In[53]:


def visualize_deformation_2d(deformation: torch.Tensor, n_rows: int, n_cols: int, **plot_kwargs) -> None:
    """Visualizes combined deformation field as deformed grid

    Args:
        deformation: Tensor with shape (2, dim_1, dim_2)
        n_rows: Number of rows
        n_cols: Number of columns
        **plot_kwargs: Keyword arguments for matplotlib plot function
    """
    transformed_grid = deformation.permute(2, 0, 1)
    for row_index in range(transformed_grid.size(1)):
        plt.plot(
            transformed_grid[1, row_index, :],
            transformed_grid[0, row_index, :],
            **plot_kwargs)
    for col_index in range(transformed_grid.size(2)):
        plt.plot(
            transformed_grid[1, :, col_index],
            transformed_grid[0, :, col_index],
            **plot_kwargs)


# In[54]:


plt.figure(figsize=(5, 5))
plt.axis('off')
plt.axis('equal')
visualize_deformation_2d(warp[0].detach().cpu(), 128, 128, color='gray', linewidth=0.7)


# In[55]:


plt.figure(figsize=(5, 5))
plt.axis('off')
plt.axis('equal')
visualize_deformation_2d(invwarp[0].detach().cpu(), 128, 128, color='gray', linewidth=0.7)


# In[106]:


invwarp = reg.get_inverse_warped_coordinates(image1, image2, smooth_warp_sigma=0.0, smooth_grad_sigma=0.0)


# In[107]:


def compose(warp1, warp2):
    grid = F.affine_grid(torch.eye(2, 3)[None], [1, 1] + list(warp1.shape[1:-1]), align_corners=True).to(warp1.device)
    w = F.grid_sample((warp1 - grid).permute(0, 3, 1, 2), warp2, align_corners=True).permute(0, 2, 3, 1) + warp2

    H, W = warp1.shape[1:-1]
    loss = (w - grid)
    loss[..., 0] *= (W-1)/2
    loss[..., 1] *= (H-1)/2
    loss = (loss**2).mean()
    
    return w, loss


# In[108]:


warp.shape[1:-1]


# In[109]:


composed, err = compose(warp, invwarp)
plt.figure(figsize=(5, 5))
plt.axis('off')
plt.axis('equal')
visualize_deformation_2d(composed[0].detach().cpu(), 128, 128, color='gray', linewidth=0.7)


# In[110]:


print(err)


# In[111]:


composed, loss = compose(invwarp, warp)
plt.figure(figsize=(5, 5))
plt.axis('off')
plt.axis('equal')
visualize_deformation_2d(composed[0].detach().cpu(), 128, 128, color='gray', linewidth=0.7)


# In[112]:


print(loss)


# In[ ]:





# In[ ]:




