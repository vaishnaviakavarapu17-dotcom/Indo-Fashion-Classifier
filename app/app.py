import streamlit as st
import tensorflow as tf
import os
import numpy as np
from PIL import Image


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Indo Fashion Classifier",
    page_icon="👗",
    layout="centered"
)


# --------------------------------------------------
# TITLE AND DESCRIPTION
# --------------------------------------------------

st.title("👗 Indo Fashion Classifier")

st.write(
    "Upload an image of clothing to classify it as "
    "Traditional or Modern."
)

st.caption(
    "CNN-based image classification using MobileNetV2 "
    "and data augmentation."
)


# --------------------------------------------------
# MODEL PATH
# --------------------------------------------------

model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "indo_fashion_augmented.keras"
)


# --------------------------------------------------
# LOAD TRAINED MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(model_path)


model = load_model()


# --------------------------------------------------
# IMAGE UPLOADER
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose a clothing image",
    type=["jpg", "jpeg", "webp", "png"]
)


# --------------------------------------------------
# PROCESS UPLOADED IMAGE
# --------------------------------------------------

if uploaded_file is not None:

    try:
        image = Image.open(uploaded_file).convert("RGB")
        
        st.image(image,caption="Uploaded Image")

    except Exception:
        st.error("The uploaded file could not be read as an image.")
        st.stop()

    # Resize image to the size expected by the model
    image = image.resize((224, 224))

    # Convert image into NumPy array
    image_array = np.array(image)

    # Normalize pixel values from 0-255 to 0-1
    image_array = image_array / 255.0

    # Add batch dimension
    image_array = np.expand_dims(image_array,axis=0)


    # --------------------------------------------------
    # MAKE PREDICTION
    # --------------------------------------------------

    prediction = model.predict(image_array,verbose=0)

    predicted_class = np.argmax(prediction[0])


    # --------------------------------------------------
    # CLASS NAMES
    # --------------------------------------------------

    class_names = ["modern","traditional"]

    predicted_class_name = class_names[predicted_class]


    # --------------------------------------------------
    # CALCULATE CONFIDENCE
    # --------------------------------------------------

    confidence = prediction[0][predicted_class]

    confidence_percentage = float(confidence * 100)

    modern_probability = float(prediction[0][0] * 100)

    traditional_probability = float(prediction[0][1] * 100)


    # --------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------

    st.subheader("Prediction")


    if predicted_class_name == "traditional":

        st.success(
            f"Traditional Clothing\n\n"
            f"Confidence: {confidence_percentage:.2f}%"
        )

    else:

        st.info(
            f"Modern Clothing\n\n"
            f"Confidence: {confidence_percentage:.2f}%"
        )


    # --------------------------------------------------
    # DISPLAY PROBABILITIES
    # --------------------------------------------------

    st.write(
        f"Modern: {modern_probability:.2f}%"
    )

    st.progress(modern_probability / 100)


    st.write(
        f"Traditional: {traditional_probability:.2f}%"
    )

    st.progress(traditional_probability / 100)


    # --------------------------------------------------
    # INFORMATION
    # --------------------------------------------------

    st.caption(
        "The confidence value represents the model's "
        "predicted probability for the selected class."
    )