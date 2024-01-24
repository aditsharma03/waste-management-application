# prediction_tab.py
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def render_prediction_tab():
    # Load your trained model
    model_path = "./custom_cnn_model2.keras"  # Replace with the actual path to your model
    model = tf.keras.models.load_model(model_path)

    # Set Streamlit app title and page layout

    # Set Streamlit app theme
    st.markdown(
        """
        <style>
            body {
                color: #FFFFFF;
                background-color: #1E1E1E;
            }
            .st-bw {
                color: #000000;
                background-color: #FFFFFF;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Streamlit app heading
    st.title("Waste Management System")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Display uploaded image
    if uploaded_file is not None:
        col1, col2 = st.columns(2)

        col1.image(uploaded_file, caption="Uploaded Image.", use_column_width=True )

        # Perform prediction on the uploaded image
        image = Image.open(uploaded_file).convert("RGB")
        image_array = np.array(image.resize((224, 224))) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)

        # Display the prediction result
        col2.subheader("Prediction Result:")
        class_indices = {'battery': 0, 'biological': 1, 'brown-glass': 2, 'cardboard': 3, 'clothes': 4,
                         'green-glass': 5, 'metal': 6, 'paper': 7, 'plastic': 8, 'shoes': 9, 'trash': 10, 'white-glass': 11}

        predicted_class_index = np.argmax(prediction)
        predicted_class_label = [key for key, value in class_indices.items() if value == predicted_class_index][0]

        waste_to_dustbin = {
                "battery": "Non-Biodegradable",
                "biological": "Biodegradable",
                "brown-glass": "Recyclable",
                "cardboard": "Recyclable",
                "clothes": "Recyclable",
                "green-glass": "Recyclable",
                "metal": "Recyclable",
                "paper": "Recyclable",
                "plastic": "Recyclable",
                "shoes": "Recyclable",
                "trash": "Non-Biodegradable",
                "white-glass": "Recyclable"
                }


        col2.write(f"The predicted class is: {predicted_class_label}")
        col2.success(f"It should be put in the {waste_to_dustbin[predicted_class_label]} bin")

