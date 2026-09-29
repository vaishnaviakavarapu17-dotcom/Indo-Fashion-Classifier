#14th
import tensorflow as tf

train_path =r"D:\Indo-Fashion Classifier\dataset_split\train"
validation_path =r"D:\Indo-Fashion Classifier\dataset_split\validation"
test_path =r"D:\Indo-Fashion Classifier\dataset_split\test"

train_dataset= tf.keras.utils.image_dataset_from_directory(
    train_path,
    image_size=(224,224),
    batch_size=32,
    shuffle=True
)
class_name =train_dataset.class_names

validation_dataset =tf.keras.utils.image_dataset_from_directory(
    validation_path,
    image_size=(224,224),
    batch_size=32,
    shuffle=False
)
test_dataset =tf.keras.utils.image_dataset_from_directory(
    test_path,
    image_size=(224,224),
    batch_size=32,
    shuffle=False
)

normalization_layer =tf.keras.layers.Rescaling(1./255)

train_dataset =train_dataset.map(
    lambda images,labels:(normalization_layer(images),labels)
)

validation_dataset =validation_dataset.map(
    lambda images,labels:(normalization_layer(images),labels)
)

test_dataset =test_dataset.map(
    lambda images,labels:(normalization_layer(images),labels)
)
print("Class Names:",class_name)