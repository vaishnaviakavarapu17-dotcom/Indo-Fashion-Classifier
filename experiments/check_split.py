#8th
##it is to check whether the train,test,validation has 
# images split accordingly or not
import os

dataset_root = r"D:\Indo-Fashion Classifier\dataset_split"

splits = ["train", "validation", "test"]
classes = ["traditional", "modern"]

for split in splits:

    print("\n", split.upper())

    for class_name in classes:

        folder = os.path.join(
            dataset_root,
            split,
            class_name
        )

        images = os.listdir(folder)

        print(class_name, ":", len(images))