#11th
from PIL import Image
import numpy as np
import os

dataset_root = r"D:\Indo-Fashion Classifier\dataset_split\train"

image_folder = os.path.join(dataset_root,"traditional")

image_files = os.listdir(image_folder)##listdir gets the filesnames inside the folder

image_path = os.path.join(image_folder,image_files[0])

image =Image.open(image_path)

print("Image selected:",image_files[0])
print("Original size:",image.size)

resized_image =image.resize((224,224))

print("Resized size:",resized_image.size)

image_array = np.array(resized_image)

print("Array shapes:",image_array.shape)
print("Data type:",image_array.dtype)

normalized_image =image_array/255.0

print("Original first pixel:",image_array[0,0])
print("Normalized first pixel:",normalized_image[0,0])