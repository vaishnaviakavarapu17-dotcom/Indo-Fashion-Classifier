#20th
import matplotlib.pyplot as plt
from PIL import Image

mistakes =[
    (
        r"D:\Indo-Fashion Classifier\dataset_split\test\modern\Dress_50.jpg",
        "modern","traditional"
    ),
    (
        r"D:\Indo-Fashion Classifier\dataset_split\test\modern\Pants_67.jpg",
        "modern","traditional"
    ),
    (
        r"D:\Indo-Fashion Classifier\dataset_split\test\traditional\lehenga_20.jpeg",
        "traditional","modern"
    )
]

plt.figure(figsize =(12,4))

for i ,(image_path,actual,predicted) in enumerate(mistakes):

    image =Image.open(image_path).convert("RGB")

    plt.subplot(1,3,i+1)

    plt.imshow(image)

    plt.title(
        f"Actual: {actual}\nPredicted: {predicted}"
    )
    plt.axis("off")

plt.tight_layout()
plt.show()