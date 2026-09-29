#26th
import tensorflow as tf

model_path =r"D:\Indo-Fashion Classifier\models\indo_fashion_transfer.keras"

test_path =r"D:\Indo-Fashion Classifier\dataset_split\test"

model =tf.keras.models.load_model(model_path)

test_dataset =tf.keras.utils.image_dataset_from_directory(
    test_path,
    image_size =(224,224),
    batch_size =32,
    shuffle =False
)
normalization_layer =tf.keras.layers.Rescaling(1./255)

test_dataset =test_dataset.map(
    lambda images,labels:(normalization_layer(images),labels)
)

#---------------------
#--Evaluate the model
#--------------------
test_loss,test_accuracy =model.evaluate(test_dataset)

print("Test Loss:",test_loss)
print("Test Accuracy:",test_accuracy)