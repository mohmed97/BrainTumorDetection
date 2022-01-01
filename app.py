
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import numpy as np
import os 
import cv2
# from PIL import Image
import tensorflow as tf
from tensorflow import keras

from keras.preprocessing.image import img_to_array

app = Flask(__name__)
   
@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
   return render_template('home.html')

@app.route('/about',methods=['GET', 'POST'])
def about():
   return render_template('about.html')

@app.route('/contact',methods=['GET', 'POST'])
def contact():
   return render_template('contact.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file =request.files["MRI_IMG"]
        if file :
            app.config['UPLOAD_FOLDER']=os.path.dirname(__file__)
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'static/images/'+filename)
            file.save(filepath)

            image = cv2.imread(filepath)
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image, (224, 224))
            image = img_to_array(image)
            image = image.reshape(1,224,224,3)
            classes = ['Glioma Tumor', 'No Tumor', 'Meningioma Tumor', 'Pituitary Tumor']
            # im = cv2.imread(filepath)
            # # myImg = np.array(im.resize(224,224))
            # myImg = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            # im_pil = Image.fromarray(myImg)
            # NewImg = myImg.reshape(1,224,224,3)
            myModel=tf.keras.models.load_model('effnet.h5')
            result = myModel.predict(image)
            output = classes[np.where(result == np.amax(result))[1][0]]
            filePath = "images/"+filename
        return render_template('result.html', predict = output,filePath = filePath)
    

if __name__ == '__main__':
   app.run()
