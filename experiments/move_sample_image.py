#10th
'''it is to move the sample image(lehenga.webp)from the 
traditional class to other new folder'''
import os
import shutil

source = r"D:\Indo-Fashion Classifier\dataset\traditional\lehenga.webp"

destination_folder = r"D:\Indo-Fashion Classifier\sample_images"

os.makedirs(destination_folder, exist_ok=True)

destination = os.path.join(
    destination_folder,
    "lehenga.webp"
)

shutil.move(source, destination)

print("Sample image moved successfully!")
print("New location:", destination)