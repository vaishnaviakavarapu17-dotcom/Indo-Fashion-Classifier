#30th
import tensorflow as tf

train_path = r"D:\Indo-Fashion Classifier\dataset_split\train"
validation_path = r"D:\Indo-Fashion Classifier\dataset_split\validation"


train_dataset = tf.keras.utils.image_dataset_from_directory(
    train_path,
    image_size=(224, 224),
    batch_size=32,
    shuffle=True
)


validation_dataset = tf.keras.utils.image_dataset_from_directory(
    validation_path,
    image_size=(224, 224),
    batch_size=32,
    shuffle=False
)


data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])


normalization_layer = tf.keras.layers.Rescaling(1./255)


train_dataset = train_dataset.map(
    lambda images, labels:
    (normalization_layer(images), labels)
)


validation_dataset = validation_dataset.map(
    lambda images, labels:
    (normalization_layer(images), labels)
)


base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)


base_model.trainable = False


model = tf.keras.Sequential([
    data_augmentation,
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(2, activation="softmax")
])


model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)


model.save(
    r"D:\Indo-Fashion Classifier\models\indo_fashion_augmented.keras"
)