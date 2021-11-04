from __future__ import print_function
#%matplotlib inline
import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Root directory for dataset
dataroot = "D:\\Python\\trainnig\\GAN\\celeba"

# We can use an image folder dataset the way we have it setup.
# Create the dataset
dataset = dset.ImageFolder(root=dataroot,
                           transform=transforms.Compose([
                               transforms.Resize(64),
                               transforms.CenterCrop(64),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                           ]))
# Create the dataloader
dataloader = torch.utils.data.DataLoader(dataset, batch_size=128,
                                         shuffle=True)


# Plot some training images
real_batch = next(iter(dataloader))
plt.figure(figsize=(8,8))
plt.axis("off")
plt.title("Training Images")
plt.imshow(np.transpose(vutils.make_grid(real_batch[0], padding=2, normalize=True).cpu(),(1,2,0)))


#--------------------------------------------------------------------------


# # Discriminative Network
# class Discriminator(nn.Module):
#     def __init__(self):
#         super(Discriminator, self).__init__()
#         self.main = nn.Sequential(
#             nn.Conv2d(in_channels= 172, out_channels= 256, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.LeakyReLU(0.2, inplace=True),#Gnet一開始丟172的圖片

#             nn.Conv2d(in_channels= 256, out_channels= 256, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(256),
#             nn.LeakyReLU(0.2, inplace=True),

#             nn.Conv2d(in_channels= 256, out_channels= 256, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(256),
#             nn.LeakyReLU(0.2, inplace=True),

#             nn.Conv2d(in_channels= 256, out_channels= 512, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(512),
#             nn.LeakyReLU(0.2, inplace=True),

#             nn.Conv2d(in_channels= 512, out_channels= 1, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(1),
#             nn.LeakyReLU(0.2, inplace=True),

#             nn.Conv2d(in_channels= 1, out_channels= 1, kernel_size= 6, stride= 1, padding=1, dilation=0),
#             nn.Sigmoid())

#     def forward(self, input):
#         return self.main(input)

# # Generative Network
# class Generator(nn.Module):
#     def __init__(self):
#         super(Generator, self).__init__()
#         self.main = nn.Sequential(
#             nn.Conv2d(in_channels= 172, out_channels= 172, kernel_size= 7, stride= 1, padding=1, dilation=0),
#             nn.LeakyReLU(0.2, inplace=True),

#             nn.Conv2d(in_channels= 172, out_channels= 256, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(256),
#             nn.LeakyReLU(0.2, inplace=True),

#             nn.Conv2d(in_channels= 256, out_channels= 512, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(512),
#             nn.LeakyReLU(0.2, inplace=True),
#             # ----------------------------------------Dilated conv1. .... 8-------------------------------------------------------------------------




#             # -----------------------------------------------------------------------------------------------------------------

#             nn.ConvTranspose2d(in_channels= 512, out_channels= 256, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(256),
#             nn.LeakyReLU(0.2, inplace=True),

#             nn.ConvTranspose2d(in_channels= 256, out_channels= 256, kernel_size= 4, stride= 1, padding=1, dilation=0),
#             nn.BatchNorm2d(256),
#             nn.LeakyReLU(0.2, inplace=True),            

#             nn.Conv2d(in_channels= 256, out_channels= 172, kernel_size= 7, stride= 1, padding=1, dilation=0),
#             nn.Tanh())

#     def forward(self, input):
#         return self.main(input)





'''
nn.Conv2d(卷積)/ nn.ConvTranspose2d(反卷積) :
in_channels：輸入的通道數目 【必選】
out_channels： 輸出的通道數目 【必選】
kernel_size：卷積核的大小，類型為int 或者元組，當卷積是方形的時候，只需要一個整數邊長即可，卷積不是方形，要輸入一個元組表示 高和寬。 【必選】
stride： 卷積每次滑動的步長為多少，默認是 1 【可選】
padding： 設置在所有邊界增加 值為 0 的邊距的大小（也就是在feature map 外圍增加幾圈 0 ），例如當 padding =1 的時候，如果原來大小為 3 × 3 ，那麼之後的大小為 5 × 5 。即在外圍加了一圈 0 。 【可選】
dilation：控製卷積核之間的間距【可選】 

nn.LeakyRelu :
negative slope，控制x為負數時的角度

nn.BatchNorm2d:
feature map 標準化
參數 = out_channels

nn.relu : 
relu稱為線性整流函數(修正線性單元)，tf.nn.relu()用於將輸入小於0的值增幅為0，輸入大於0的值不變。

nn.Tanh :
function to return it to the input data range of [-1,1]
'''