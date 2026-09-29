#9th
"""this code is to check
according to the check_split code it said the traditional class
has 501 images instead of 500 images and modern has 500 images
as if now we just want only 500 images in both the clases.
This code used to find the where the extra image is"""
import os

dataset_root = r"D:\Indo-Fashion Classifier\dataset_split"
'''root = train
folder =classes[traditional,modern]
files =images in the classes'''
for root,folder,files in os.walk(dataset_root):

    for file in files:
        
        if file == "lehenga.webp":

            print("Found lehenga.webp")
            print("Location:",os.path.join(root,file))