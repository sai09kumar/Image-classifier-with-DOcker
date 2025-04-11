import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Load MobileNetV2 model with pre-trained weights
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Function to preprocess image for the model
def preprocess_image(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array

# Use the model to classify the image
def classify_image(path):
    img = preprocess_image(path)
    preds = model.predict(img)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0]
    return f"{decoded[1]} ({decoded[2]*100:.2f}%)"

# GUI setup
app = tk.Tk()
app.title("Image Classifier AI")
app.geometry("400x500")

label = tk.Label(app, text="Upload an Image", font=("Arial", 16))
label.pack(pady=10)

img_label = tk.Label(app)
img_label.pack()

result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Handle button click
def upload_and_classify():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Show image
        img = Image.open(file_path).resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk

        # Classify with AI
        result = classify_image(file_path)
        result_label.config(text="Prediction: " + result)

# Button to upload image
upload_btn = tk.Button(app, text="Upload Image", command=upload_and_classify)
upload_btn.pack(pady=20)

# Run the app
app.mainloop()
