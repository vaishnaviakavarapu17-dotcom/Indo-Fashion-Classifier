#19th
import tensorflow as tf
import numpy as np
import os

model_path = r"D:\Indo-Fashion Classifier\models\indo_fashion_cnn.keras"
test_path = r"D:\Indo-Fashion Classifier\dataset_split\test"

model = tf.keras.models.load_model(model_path)

test_dataset = tf.keras.utils.image_dataset_from_directory(
    test_path,
    image_size=(224, 224),
    batch_size=32,
    shuffle=False
)

class_names = test_dataset.class_names

image_paths = test_dataset.file_paths

normalization_layer = tf.keras.layers.Rescaling(1./255)

test_dataset = test_dataset.map(
    lambda images, labels:
    (normalization_layer(images), labels)
)


true_labels = []
predicted_labels = []

for images, labels in test_dataset:

    predictions = model.predict(images, verbose=0)

    predicted_classes = np.argmax(predictions, axis=1)

    true_labels.extend(labels.numpy())
    predicted_labels.extend(predicted_classes)

for i in range(len(true_labels)):

    if true_labels[i] != predicted_labels[i]:

        print("\nMisclassified Image:")
        print("Image:", image_paths[i])
        print("Actual:", class_names[true_labels[i]])
        print("Predicted:", class_names[predicted_labels[i]])