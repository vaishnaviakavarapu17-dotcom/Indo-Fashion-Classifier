#17th
import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

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

cm = confusion_matrix(true_labels, predicted_labels)

print("\nClass Names:")
print(class_names)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(
    classification_report(
        true_labels,
        predicted_labels,
        target_names=class_names
    )
)