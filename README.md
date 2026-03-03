# 👁️ Vision AI: Image Classification App

A Deep Learning web application that can "see" and identify objects in images. 
Built with **Python**, **TensorFlow**, and **Streamlit**, this app uses a Convolutional Neural Network (CNN) to classify images into 10 distinct categories with high accuracy.

🔴 **[Live Demo](https://jm7fe8d8zkqwwgbb3wuqjo.streamlit.app/)**

---

## 🚀 Features
* **Drag-and-Drop Interface:** Upload any `.jpg` or `.png` image directly from your computer.
* **Real-Time Analysis:** The AI processes the image in milliseconds.
* **10-Class Detection:** Capable of identifying:
    * ✈️ Airplanes
    * 🚗 Automobiles
    * 🐦 Birds
    * 🐱 Cats
    * 🦌 Deer
    * 🐶 Dogs
    * 🐸 Frogs
    * 🐴 Horses
    * 🚢 Ships
    * 🚚 Trucks
* **Confidence Scoring:** Displays the AI's certainty percentage for each prediction.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Deep Learning:** TensorFlow / Keras (CNN Architecture)
* **Web Framework:** Streamlit
* **Data Processing:** NumPy, Pillow (PIL)

---

## 🧠 How It Works (The AI Model)
The core of this project is a **Convolutional Neural Network (CNN)** trained on the **CIFAR-10** dataset (60,000 color images). 

Unlike standard neural networks that flatten images into a list of numbers, this model uses **Conv2D** layers to scan the image for 2D geometric features:
1.  **Input Layer:** Accepts 32x32 pixel RGB images.
2.  **Convolutional Layers:** Scans for edges, curves, and textures.
3.  **MaxPooling:** Reduces dimensionality to focus on the most important features.
4.  **Dense Layers:** Interprets the features and outputs a probability for each of the 10 categories.

---

*Created by Prathamesh as part of a 15-Day Data Science Sprint.*
