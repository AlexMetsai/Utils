'''
Search recursively for all images in the current working directory 
and apply saturation, with regard to a user defined threshold.

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

import os
from imageio import imsave, imread

# Define saturation threshold
THRESHOLD = 40
# You can use other or a number of formats. To do so,
# create a tuple/list, example: [".jpg", ".png"]
ext = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

if __name__ == '__main__':
  
    # Continue only if user replies "Yes"
    print("\nThis script will recursively saturate all images in your"+
  	  " current working directory. Are you sure you want to continue? (y/n)")
    x= input()
    if (x!='y' and x!="Y"): exit()
  
    # Find all files bellow the working directory
    # and apply saturation, replacing their originals.
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.endswith(ext):
        
                # load image
                im_path = os.path.relpath(os.path.join(root, f), ".")
                im = imread(im_path)
                
                # saturate image
                for i in range(im.shape[0]):
                    for j in range(im.shape[1]):
                        for k in range(im.shape[2]):
                            if im[i, j, k] > THRESHOLD:
                                im[i, j, j] = 255
                            else:
                                im[i, j, k] = 0
                
                # Save image
                imsave = (im_path, im)
    print("All images saturated successfully.")
