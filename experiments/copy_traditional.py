#4th
import json
import os
import shutil ##it gives us func's for working with files

# Location of the downloaded IndoFashion dataset
source_root = r"C:\Users\akava\Downloads\indo-fashion"

# Location where we want our Traditional images
destination = r"D:\Indo-Fashion Classifier\dataset\traditional"

# Traditional categories we selected
categories = {
    "saree": 100,
    "lehenga": 80,
    "women_kurta": 80,
    "kurta_men": 60,
    "sherwanis": 40,
    "dhoti_pants": 40,
    "nehru_jackets": 40,
    "dupattas": 30,
    "petticoats": 30
}

# Create destination folder if it doesn't exist
os.makedirs(destination, exist_ok=True)

# Keep track of how many images we copied
copied = {}

for category in categories:
    copied[category] = 0

# Read the JSON file
json_file = os.path.join(source_root, "train_data.json")

with open(json_file, "r") as file:

    for line in file:

        if not line.strip():
            continue

        data = json.loads(line)

        label = data["class_label"]

        # Check whether this is one of our selected categories
        if label not in categories:
            continue

        # Stop collecting this category when its quota is reached
        if copied[label] >= categories[label]:
            continue

        # Get the image path
        image_path = os.path.join(source_root, data["image_path"])

        # Make sure the image actually exists
        if not os.path.exists(image_path):
            continue

        # Create a new filename
        new_name = f"{label}_{copied[label] + 1}.jpeg"

        destination_path = os.path.join(destination, new_name)

        # Copy the image
        shutil.copy2(image_path, destination_path)

        copied[label] += 1

        # Stop when all categories are complete
        if sum(copied.values()) == sum(categories.values()):
            break


print("\nTraditional dataset created!")
print("--------------------------------")

for category in copied:
    print(category, ":", copied[category])

print("--------------------------------")
print("Total images:", sum(copied.values()))