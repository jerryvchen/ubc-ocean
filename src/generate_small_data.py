# Temporarly create a set of processed images

# this will not be executed as part of the project, rather it is 
# here to generate the data set needed for the project report

import cv2
import numpy as np
import os

# input/output directories
input_folder = "./data/train_thumbnails"
output_folder = "./small_data"

os.makedirs(output_folder, exist_ok=True)

target_size = (256, 256) # arbitrary size

file_list = os.listdir(input_folder)

for f in file_list:
    img = cv2.imread(os.path.join(input_folder, f))
    
    original_height, original_width, _ = img.shape
    
    # aspect ratio
    aspect_ratio = original_width / original_height
    
    # calc new dims based on ratio
    if aspect_ratio > 1:
        new_width = target_size[0]
        new_height = int(target_size[0] / aspect_ratio)
    else:
        new_width = int(target_size[1] * aspect_ratio)
        new_height = target_size[1]
    
    # resize image,preserving aspect ratio
    resized_img = cv2.resize(img, (new_width, new_height))
    
    # black canvas of the target size
    canvas = 0 * np.ones((target_size[1], target_size[0], 3), dtype=np.uint8) 
    
    # calc the pos to paste resized
    x_offset = (target_size[0] - new_width) // 2
    y_offset = (target_size[1] - new_height) // 2
    
    # put resized image onto the canvas
    canvas[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_img
    
    # Save the canvas as the resized image
    cv2.imwrite(os.path.join(output_folder, f), canvas)
print("Finished image processing")