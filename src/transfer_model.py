#24th
import tensorflow as tf

base_model =tf.keras.applications.MobileNetV2(
    input_shape =(224,224,3),
    include_top =False,
    weights ="imagenet"
)

base_model.trainable =False

model =tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(2,activation ="softmax")
])

model.compile(
    optimizer ="adam",
    loss ="sparse_categorical_crossentropy",
    metrics =["accuracy"]
)
model.summary()