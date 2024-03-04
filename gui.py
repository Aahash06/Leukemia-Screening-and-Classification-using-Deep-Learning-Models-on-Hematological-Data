import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

# Load the trained model
neural_network_model = load_model(r"F:\Cancer Pred\Neural_network_model.h5")

# Define the class labels
class_labels = ["EarlyPreB", "PreB", "ProB", "Benign" ]

# Define the desired input shape for the model
desired_input_shape = (128, 128)  # Adjust according to your model's input shape

# Function to preprocess input data
def preprocess_input_data(input_data):
    # Resize input image to the desired shape
    resized_image = cv2.resize(input_data, (desired_input_shape[0], desired_input_shape[1]))
    # Normalize image
    normalized_image = resized_image / 255.0
    # Expand dimensions to match model's input shape
    preprocessed_input_data = np.expand_dims(normalized_image, axis=0)
    return preprocessed_input_data

def load_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Read the selected image
        input_image = cv2.imread(file_path)

        # Preprocess the input data
        preprocessed_input_data = preprocess_input_data(input_image)

        # Make predictions using the loaded model
        predictions = neural_network_model.predict(preprocessed_input_data)

        # Get the index of the class with the highest probability
        predicted_class_index = np.argmax(predictions)

        # Determine the predicted class label
        predicted_class = class_labels[predicted_class_index]

        # Display the input image with the predicted class as the title
        plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
        plt.title(f"Predicted Class: {predicted_class} (Probabilities: {predictions[0]})")
        plt.axis('off')
        plt.show()

# Create the main window
root = tk.Tk()
root.title("Cancer Prediction")

# Create a button to load an image
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

# Run the application
root.mainloop()
