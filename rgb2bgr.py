'''
Convert all images current working dir to BGR.
If images are already in BGR, they will be converted to RGB.

Copyright (C) 2019 Alexandros I. Metsai
alexmetsai@gmail.com

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import numpy as np
import cv2
import os
from scipy import ndimage
from imageio import imsave, imread

ext = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

if __name__ == '__main__':
    # Continue only if user replies "Yes"
    print("\nThis script will recursively manipulate all images in your"+
          " current working directory. Are you sure you want to continue? (y/n)")
    x = input()
    if (x!='y' and x!="Y"): 
        exit()
    
    # Find all files bellow the working directory and convert 
    # them to BGR, replacing their originals.
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.endswith(ext):
                
                # load image
                im_path = os.path.relpath(os.path.join(root, f), ".")
                print("Resizing " + im_path)
                im = imread(im_path)
                
                # RGB to BGR
                bgr = np.zeros(im.shape, dtype=int)
                bgr[:,:,:] = im[:,:,:]
                bgr[:,:,0] = im[:,:,2]
                bgr[:,:,1] = im[:,:,1]
                bgr[:,:,2] = im[:,:,0]
                
                # Save image
                imsave(im_path, bgr)
                
    print("Resized all frames successfully.")
