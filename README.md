# Skin Disease Diagnosis Project

## Description

This project is a web application that uses a machine learning model to diagnose skin diseases based on uploaded images. Users can upload images of their skin lesions and receive a prediction of the possible condition.

## Features

* Upload images of skin lesions.
* Diagnose the condition using a trained machine learning model.
* Display the predicted diagnosis and detailed information (if available).
* Allow users to report inaccurate results.

## Technologies Used

* **Backend:** [Python/Flask/Django/...] (choose one or more)
* **Machine Learning:** [TensorFlow/Keras/PyTorch/...] (choose one)
* **Frontend:** HTML, CSS, JavaScript
* **Other:** [Docker/SQLAlchemy/...] (add if applicable)

## Folder Structure
skin-notebook/
├── app/
│ ├── static/
│ │ ├── css/
│ │ └── js/
│ ├── templates/
│ └── app.py (or your main file name)
├── model/
│ └── model.h5 (or your model file name)
├── requirements.txt
└── README.md
## Installation
### Warming: sure that using Python 3.10 to compile this project
1. Clone the repository: `git clone https://github.com/NienCongChua/skin-notebook.git`
2. Create a virtual environment: `python3.10 -m venv env`
3. Activate the virtual environment: `source env/bin/activate`
4. Install the required libraries: `pip install -r requirements.txt`
5. Run the application: `python app/app.py` (or your respective command)

## Usage

1. Open a web browser and go to `http://127.0.0.1:5000/` (or the specified address).
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
