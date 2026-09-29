#6th
import csv
import os
import shutil

source_root = r"C:\Users\akava\Downloads\archive (1)"
destination = r"D:\Indo-Fashion Classifier\dataset\modern"

categories = {
    "T-Shirt": 100,
    "Shirt": 70,
    "Pants": 80,
    "Shorts": 40,
    "Skirt": 30,
    "Outwear": 50,
    "Dress": 60,
    "Longsleeve": 30,
    "Polo": 20,
    "Hoodie": 10,
    "Blazer": 10
}

os.makedirs(destination, exist_ok=True)

copied = {}

for category in categories:
    copied[category] = 0

csv_file = os.path.join(source_root, "images.csv")

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        label = row["label"]
        kids = row["kids"]

        if label not in categories:
            continue

        if kids != "False":
            continue

        if copied[label] >= categories[label]:
            continue

        image_name = row["image"] + ".jpg"

        image_path = os.path.join(
            source_root,
            "images_original",
            image_name
        )

        if not os.path.exists(image_path):
            continue

        new_name = f"{label}_{copied[label] + 1}.jpg"

        destination_path = os.path.join(
            destination,
            new_name
        )

        shutil.copy2(image_path, destination_path)

        copied[label] += 1

        if sum(copied.values()) == sum(categories.values()):
            break

print("\nModern dataset created!")
print("--------------------------------")

for category in copied:
    print(category, ":", copied[category])

print("--------------------------------")
print("Total images:", sum(copied.values()))