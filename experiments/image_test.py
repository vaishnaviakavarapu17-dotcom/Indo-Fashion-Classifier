##1st
from PIL import Image
import numpy as np
image =Image.open("dataset/traditional/lehenga.webp")

image_array =np.array(image)

print("Before Normalization:")
print("Data Type:",image_array.dtype)
print("First Pixel:",image_array[0,0])

normalized_image =image_array/255.0

print("After Normalization:")
print("Data Type:",normalized_image.dtype)
print("First Pixel:",normalized_image[0,0])

##.shape gives the dimensions and RGB values(eg,380,380,3)