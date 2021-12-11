
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import numpy as np
import os 

app = Flask(__name__)
   
@app.route('/',methods=['GET', 'POST'])
def home():
   return render_template('home.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file =request.files["MRI_IMG"]
        if file :
            app.config['UPLOAD_FOLDER']=os.path.dirname(__file__)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html')
    

if __name__ == '__main__':
   app.run()
