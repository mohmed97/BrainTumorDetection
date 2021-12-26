
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import numpy as np
import os 
import cv2
import tensorflow as tf 
from tensorflow import keras

app = Flask(__name__)
   
@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
   return render_template('home.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
   return render_template('about.html')
 
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file =request.files["MRI_IMG"]
        if file :
            app.config['UPLOAD_FOLDER']=os.path.dirname(__file__)
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded/images/'+filename)
            file.save(filepath)
            myImg = cv2.resize(cv2.imread(filepath), (224,224))
            myModel=tf.keras.models.load_model('effnet.h5')
            # result = myModel.predict(myImg)
            # ,predict=result
        return render_template('result.html')
    

if __name__ == '__main__':
   app.run()
