import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

@st.cache_resource
def load_vision_ai():
    return tf.keras.models.load_model('cifar_color_model.keras')

model = load_vision_ai()

class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 
               'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

st.title("Vision AI: Image Classifier 👁️")
st.write("Upload a picture of an airplane, car, bird, cat, deer, dog, frog, horse, ship, or truck!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    st.write("🧠 AI is analyzing...")
    
    img_resized = image.resize((32, 32)) 
    img_array = np.array(img_resized)
    
    if img_array.shape[-1] == 4:
        img_array = img_array[..., :3]
        
    img_array = img_array / 255.0
    
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction) * 100
    
    st.success(f"**AI Prediction:** {class_names[predicted_class]}")
    st.info(f"**Confidence Level:** {confidence:.2f}%")