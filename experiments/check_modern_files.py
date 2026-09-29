#5th
import csv
import os

source_root = r"C:\Users\akava\Downloads\archive (1)"

csv_file = os.path.join(source_root, "images.csv")
images_folder = os.path.join(source_root, "images_original")

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["label"] == "T-Shirt" and row["kids"] == "False":

            image_name = row["image"]

            print("CSV image name:")
            print(repr(image_name))

            matches = [
                file_name
                for file_name in os.listdir(images_folder)
                if file_name.startswith(image_name)
            ]

            print("\nMatching files in images_original:")
            print(matches[:5])

            break