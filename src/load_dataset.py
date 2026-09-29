#12th
import tensorflow as tf

train_path =r"D:\Indo-Fashion Classifier\dataset_split\train"

train_dataset =tf.keras.utils.image_dataset_from_directory(
    train_path,
    image_size =(224,224),
    batch_size =32
)
print("Class Names:",train_dataset.class_names)
print("Number of batches:",len(train_dataset))

images,labels =next(iter(train_dataset))

print("Image batch shape:",images.shape)
print("Label batch shape:",labels.shape)

normalized_layer =tf.keras.layers.Rescaling(1./255)

normalized_images = normalized_layer(images)

print("Original first pixel:",images[0,0,0].numpy())
print("Normalized first pixel:",normalized_images[0,0,0].numpy())