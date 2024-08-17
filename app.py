import os
import glob
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.preprocessing.image import load_img, img_to_array #type: ignore

app = Flask(__name__)

MODEL_PATH = 'skin_disease_cnn_model_newv2.keras'

model = tf.keras.models.load_model(MODEL_PATH)

class_names = [
    'Actinic Keratoses and Intraepithelial Carcinoma (Bowen\'s Disease)',  # akiec
    'Basal Cell Carcinoma',  # bcc
    'Benign Keratosis-like Lesions',  # bkl
    'Dermatofibroma',  # df
    'Melanoma',  # mel
    'Melanocytic Nevi',  # nv
    'Vascular Lesions'  # vasc
]

def delete_all_image_files_in_static():
    folder = 'static'
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif']
    
    for ext in image_extensions:
        files = glob.glob(os.path.join(folder, ext))
        for f in files:
            try:
                os.remove(f)
                print(f"Deleted: {f}")
            except Exception as e:
                print(f"Error deleting file {f}: {e}")


def model_predict(img_path, model, class_names, confidence_threshold=0.8):
    img = load_img(img_path, target_size=(192, 192))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    predicted_class_index = np.argmax(preds[0])
    predicted_class_confidence = preds[0][predicted_class_index]

    if predicted_class_confidence < confidence_threshold:
        return "Unknown"
    else:
        predicted_class = class_names[predicted_class_index]
        return predicted_class


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    delete_all_image_files_in_static()
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join('static', file.filename)
        file.save(file_path)

        predicted_class = model_predict(file_path, model, class_names)
        print(file.filename)
        return render_template('index.html', prediction=predicted_class, img_path=file.filename)

if __name__ == '__main__':
    app.run(debug=True)
