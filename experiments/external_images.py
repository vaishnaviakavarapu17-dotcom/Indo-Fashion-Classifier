#22th
import tensorflow as tf
import numpy as np
import os
from PIL import Image

model_path =r"D:\Indo-Fashion Classifier\models\indo_fashion_cnn.keras"

external_folder =r"D:\Indo-Fashion Classifier\external_images"

class_names =["modern","traditional"]

model =tf.keras.models.load_model(model_path)

image_files =os.listdir(external_folder)

for image_file in image_files:
    
    image_path =os.path.join(external_folder,image_file)
    image =Image.open(image_path).convert("RGB")
    image =image.resize((224,224))
    image_array =np.array(image)
    image_array =image_array / 255.0

    image_array =np.expand_dims(image_array,axis =0)
    prediction =model.predict(image_array,verbose =0)
    predicted_class =np.argmax(prediction[0])

    confidence =prediction[0][predicted_class]

    print("\nImages:",image_file)
    print("Predicted:",class_names[predicted_class])
    print("Confidence:",confidence * 100,"%")
    print("Modern Probability:",prediction[0][0]*100,"%")
    print("Traditional_Probability:",prediction[0][1]*100,"%")
