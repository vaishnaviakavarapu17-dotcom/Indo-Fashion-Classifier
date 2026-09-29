#21th
import tensorflow as tf
import numpy as np
from PIL import Image

model_path =r"D:\Indo-Fashion Classifier\models\indo_fashion_cnn.keras"

mistakes =[
    (
        r"D:\Indo-Fashion Classifier\dataset_split\test\modern\Dress_50.jpg",
        "modern"
    ),
    (
        r"D:\Indo-Fashion Classifier\dataset_split\test\modern\Pants_67.jpg",
        "modern"
    ),
    (
        r"D:\Indo-Fashion Classifier\dataset_split\test\traditional\lehenga_20.jpeg",
        "traditional"
    )
]

class_names =["modern","traditional"]

model =tf.keras.models.load_model(model_path)

for image_path,actual_class in mistakes:

    image =Image.open(image_path).convert("RGB")
    image =image.resize((224,224))
    image_array =np.array(image)
    image_array =image_array / 255.0

    image_array =np.expand_dims(image_array,axis =0)
    prediction =model.predict(image_array,verbose =0)
    predicted_class =np.argmax(prediction[0])

    confidence =prediction[0][predicted_class]

    print("\nImage:",image_path)
    print("Actual:",actual_class)
    print("Predicted:",class_names[predicted_class])
    print("Confidence:",confidence * 100,"%")

    print("Modern Probability:",prediction[0][0] * 100,"%")
    print("Traditioanl_probability:",prediction[0][1] *100,"%")