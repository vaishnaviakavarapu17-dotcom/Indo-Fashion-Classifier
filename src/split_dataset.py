#7th
import os
import random
import shutil


# Where our original dataset is
source_root = r"D:\Indo-Fashion Classifier\dataset"

# Where we will create train/validation/test
destination_root = r"D:\Indo-Fashion Classifier\dataset_split"


# The two classes in our project
classes = ["traditional", "modern"]


# Dataset split percentages
train_ratio = 0.70
validation_ratio = 0.15
test_ratio = 0.15


# Makes the random split reproducible
random.seed(42)


# Image file extensions we will accept
valid_extensions = (".jpg", ".jpeg", ".png", ".webp")


# --------------------------------------------------
# Step 1: Check the original dataset
# --------------------------------------------------

for class_name in classes:

    source_folder = os.path.join(
        source_root,
        class_name
    )

    images = [
        file
        for file in os.listdir(source_folder)
        if file.lower().endswith(valid_extensions)
    ]

    print(class_name, "images found:", len(images))

    if len(images) != 500:
        print("Error: Expected exactly 500 images.")
        exit()


# --------------------------------------------------
# Step 2: Remove the old split
# --------------------------------------------------

if os.path.exists(destination_root):

    shutil.rmtree(destination_root)

    print("\nOld dataset_split removed.")


# --------------------------------------------------
# Step 3: Create the new split
# --------------------------------------------------

for class_name in classes:

    source_folder = os.path.join(
        source_root,
        class_name
    )

    images = [
        file
        for file in os.listdir(source_folder)
        if file.lower().endswith(valid_extensions)
    ]

    random.shuffle(images)

    total_images = len(images)

    train_count = int(total_images * train_ratio)

    validation_count = int(
        total_images * validation_ratio
    )

    train_images = images[:train_count]

    validation_images = images[
        train_count:
        train_count + validation_count
    ]

    test_images = images[
        train_count + validation_count:
    ]

    for split_name, split_images in [
        ("train", train_images),
        ("validation", validation_images),
        ("test", test_images)
    ]:

        destination_folder = os.path.join(
            destination_root,split_name,class_name)

        os.makedirs(destination_folder,exist_ok=True)

        for image in split_images:

            source_path = os.path.join(source_folder,image)

            destination_path = os.path.join(destination_folder,image)

            shutil.copy2(source_path,destination_path)

    print(class_name, "split completed")


print("\nDataset splitting completed!")