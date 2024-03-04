# Leukemia-Screening-and-Classification-using-Deep-Learning-Models-on-Hematological-Data
Overview
This project aims to develop and evaluate deep learning models for the screening and classification of Acute Lymphoblastic Leukemia (ALL) using peripheral blood smear (PBS) images. The dataset used in this project is sourced from Kaggle and consists of a large collection of PBS images obtained from patients suspected of having ALL.

Dataset
The dataset contains 3242 PBS images collected from 89 patients suspected of ALL, prepared and stained by skilled laboratory staff at Taleqani Hospital in Tehran, Iran. The images are divided into two classes: benign and malignant. The malignant class includes three subtypes of malignant lymphoblasts: Early Pre-B, Pre-B, and Pro-B ALL. Each image is captured using a Zeiss camera mounted on a microscope with a magnification of 100x and saved in JPG format.

The definitive determination of the types and subtypes of cells depicted in the images was made by a specialist using the flow cytometry tool.

Objective
The definitive diagnosis of ALL often requires invasive, expensive, and time-consuming diagnostic tests. PBS images offer a less invasive and more accessible approach for initial screening. However, manual examination of these images is prone to diagnostic errors due to the non-specific nature of ALL signs and symptoms.

The objective of this project is to develop deep learning models capable of accurately screening and classifying ALL based on PBS images. These models can potentially aid in improving diagnostic accuracy, reducing misdiagnosis rates, and facilitating early detection and treatment of ALL.

Project Structure
train.ipynb: Jupyter Notebook containing code for training deep learning models on the dataset.
predict.ipynb: Jupyter Notebook containing code for making predictions using trained models.
gui.py: Python script for building a graphical user interface (GUI) for interacting with the models.
Blood Cell CNN.ipynb: Jupyter Notebook containing code for developing a convolutional neural network (CNN) model specifically for blood cell classification.
/Labs Samples: Directory containing additional sample images for testing and validation purposes.
Usage
Training Models: Open and run train.ipynb to train deep learning models on the dataset.
Making Predictions: Use predict.ipynb to make predictions on new PBS images using trained models.
Graphical User Interface: Run gui.py to interact with the trained models via a graphical user interface.
Blood Cell CNN Model: Explore Blood Cell CNN.ipynb for developing a CNN model specifically for blood cell classification.
Acknowledgments
Dataset Source: Blood Cells Cancer (ALL) dataset on Kaggle
Taleqani Hospital: For providing the PBS images used in the dataset.
Specialist: For definitive determination of cell types and subtypes.
License
This project is licensed under the MIT License.
