#23rd
import matplotlib.pyplot as plt
from PIL import Image
import os


test_traditional_folder = r"D:\Indo-Fashion Classifier\dataset_split\test\traditional"

external_folder = r"D:\Indo-Fashion Classifier\external_images"


# Find one test image for each clothing type
test_files = os.listdir(test_traditional_folder)

lehenga_test = next(
    file for file in test_files
    if file.startswith("lehenga_")
)

saree_test = next(
    file for file in test_files
    if file.startswith("saree_")
)

kurta_test = next(
    file for file in test_files
    if file.startswith("kurta_men_")
)


comparisons = [
    (
        os.path.join(test_traditional_folder, lehenga_test),
        os.path.join(external_folder, "lehenga1.jpg"),
        "Lehenga"
    ),
    (
        os.path.join(test_traditional_folder, saree_test),
        os.path.join(external_folder, "saree.jpg"),
        "Saree"
    ),
    (
        os.path.join(test_traditional_folder, kurta_test),
        os.path.join(external_folder, "kurta.jpg"),
        "Kurta"
    )
]


plt.figure(figsize=(12, 9))


for i, (test_path, external_path, clothing_type) in enumerate(comparisons):

    test_image = Image.open(test_path).convert("RGB")

    external_image = Image.open(external_path).convert("RGB")


    plt.subplot(3, 2, i * 2 + 1)

    plt.imshow(test_image)

    plt.title(
        f"{clothing_type}\nTraining/Test Dataset"
    )

    plt.axis("off")


    plt.subplot(3, 2, i * 2 + 2)

    plt.imshow(external_image)

    plt.title(
        f"{clothing_type}\nExternal Image"
    )

    plt.axis("off")


plt.tight_layout()

plt.show()