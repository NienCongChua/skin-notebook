# Skin Disease Diagnosis Project

## Description

This project is a web application that uses a machine learning model to diagnose skin diseases based on uploaded images. Users can upload images of their skin lesions and receive a prediction of the possible condition.

## Features

* Upload images of skin lesions.
* Diagnose the condition using a trained machine learning model.
* Display the predicted diagnosis and detailed information (if available).
* Allow users to report inaccurate results.

## Technologies Used

* **Backend:** Python, Flask 
* **Machine Learning:** TensorFlow
* **Frontend:** HTML, CSS, JavaScript
* **Other:** None

## Folder Structure
skin-notebook/\
│\
├── data3/\
│ ├── test/\
│ └── train/\
│\
├── static/\
│ ├── script.js\
│ └── style.css\
│\
├── templates/\
│ └── index.html\
│\
├── requirements.txt\
├── app.py\
├── disease_details.json\
├── predict-colab.ipynb\
├── predict.ipynb\
├── skin_disease_cnn_model_newv2.keras\
└── README.md

## Installation
### Warming: sure that using Python 3.10 to compile this project
1. Clone the repository: `git clone https://github.com/NienCongChua/skin-notebook.git`
2. Download the directory data from the link: [data3](https://yy17z-my.sharepoint.com/:f:/g/personal/lechingan_yy17z_onmicrosoft_com/Emy6JB8WlnNAkVeYm2aa200B6EFpU8sdkfsGp9z8XbFw1g?e=Y0500R) or [`alternative data3`](https://drive.google.com/file/d/1Q0MwLhwZ1y8orO4kIakpxJl6hU9bDeip/view?usp=drive_link) to train the model. (Option)
3. Create a virtual environment: `python3.10 -m venv env`
4. Activate the virtual environment: `source env/bin/activate`
5. Install the required libraries: `pip install -r requirements.txt`
6. Run the application: `python app.py`

## Usage

1. Open a web browser and go to `http://127.0.0.1:5000/`.
2. Choose an image of the skin lesion you want to diagnose.
3. Click the "Upload and Predict" button.
4. View the predicted diagnosis displayed below.
5. If you have any questions, please click "Report".

## Limitations

* The accuracy of the model depends on the quality and quantity of the training data.
* This application should not be used for self-diagnosis or treatment.
* Always consult with a healthcare professional for accurate diagnosis and treatment.

## Author

* Richard Jacob - https://github.com/NienCongChua/
* Pham Thanh Dat - https://github.com/LewPie/
