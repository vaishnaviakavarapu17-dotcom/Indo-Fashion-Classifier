#29th
import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image


model_path = r"D:\Indo-Fashion Classifier\models\indo_fashion_transfer.keras"

external_path = r"D:\Indo-Fashion Classifier\external_images"


model = tf.keras.models.load_model(model_path)


class_names = ["modern", "traditional"]


image_files = os.listdir(external_path)


for image_file in image_files:

    image_path = os.path.join(external_path, image_file)

    image = Image.open(image_path).convert("RGB")

    original_image = image.copy()

    image = image.resize((224, 224))

    image_array = np.array(image)

    image_array = image_array / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array, verbose=0)

    predicted_class = np.argmax(prediction[0])

    confidence = prediction[0][predicted_class]

    modern_probability = prediction[0][0]

    traditional_probability = prediction[0][1]


    plt.figure(figsize=(6, 5))

    plt.imshow(original_image)

    plt.title(
        f"File: {image_file}\n"
        f"Predicted: {class_names[predicted_class]}\n"
        f"Confidence: {confidence * 100:.2f}%\n"
        f"Modern: {modern_probability * 100:.2f}%\n"
        f"Traditional: {traditional_probability * 100:.2f}%"
    )

    plt.axis("off")

    plt.show()