#15th
import tensorflow as tf

train_path =r"D:\Indo-Fashion Classifier\dataset_split\train"
validation_path =r"D:\Indo-Fashion Classifier\dataset_split\validation"

train_dataset =tf.keras.utils.image_dataset_from_directory(
    train_path,
    image_size=(224,224),
    batch_size =32,
    shuffle =True
)
class_name =train_dataset.class_names

validation_dataset =tf.keras.utils.image_dataset_from_directory(
    validation_path,
    image_size =(224,224),
    batch_size =32,
    shuffle =False
)
normalization_layer =tf.keras.layers.Rescaling(1./255)

train_dataset =train_dataset.map(
    lambda images,labels:(normalization_layer(images),labels)
)

validation_dataset =validation_dataset.map(
    lambda images,labels:(normalization_layer(images),labels)
)
#--------------------------
#-----Create CNN model-----
#--------------------------

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape =(224,224,3)),
    tf.keras.layers.Conv2D(32,(3,3),activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    tf.keras.layers.Conv2D(64,(3,3),activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64,activation="relu"),
    tf.keras.layers.Dense(2,activation="softmax")
])
#------------------------
#----Compile the model----
#-------------------------

model.compile(
    optimizer ="adam",
    loss ="sparse_categorical_crossentropy",
    metrics =["accuracy"]   
)

#-----------------------
#----train the model----
#-----------------------

history =model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs =10
)

#------------------------------
#----Save the trained model----
#------------------------------
model_path = r"D:\Indo-Fashion Classifier\models\indo_fashion_cnn.keras"
model.save(model_path)
print("Model saved successfully")
print("Saved path:",model_path)