#18th
import tensorflow as tf
import numpy as np
from PIL import Image

model_path =r"D:\Indo-Fashion Classifier\models\indo_fashion_cnn.keras"
image_path =r"D:\Indo-Fashion Classifier\sample_images\lehenga.webp"

model =tf.keras.models.load_model(model_path)
image =Image.open(image_path).convert("RGB")

image =image.resize((224,224))
image_array =np.array(image)

image_array =image_array/255.0

image_array =np.expand_dims(image_array,axis =0)

prediction =model.predict(image_array,verbose =0)

predicted_class =np.argmax(prediction[0])

confidence =prediction[0][predicted_class]

class_name =["modern","traditional"]

print("Raw prediction:",prediction[0])
print("Modern probability:",prediction[0][0])
print("Traditional probability:",prediction[0][1])
print("Predicted class:",class_name[predicted_class])
print("Confidence:",confidence * 100,"%")