from app import app
import csv
import numpy as np
from flask import render_template, redirect, request,\
      flash, url_for
import os
import pandas as pd
import pickle
from werkzeug.utils import secure_filename

@app.route('/')
def index():
    return render_template('public/index.html')


def allowed_file(filename):
        """function checks if an extension is valid,
        :checks for the dot and rplit and check for lower case
        and uploads the file and direct the user to
        the URL to upload file"""
        return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_FILE_EXTENSIONS']

def allowed_filesize(filesize):
    """function checks for filesize as specified in
      MAX_CONTENT_LENGHT  """
    return int(filesize) <= app.config['MAX_CONTENT_LENGHT']

@app.route('/upload-file', methods=['GET','POST'])
def file_upload():
    """ function takes upload and
      make prediction on file"""
    if request.method == 'POST':
    
       if request.files: 

           if not allowed_filesize(request.cookies.get('filesize')): 
               flash('filesize exceeds maximum')
               return redirect(url_for('file_upload'))
           
           file = request.files['file'] # store our variable here and access the image in our html

           if 'file' not in request.files: # check if the post request has the file part
                flash('NO file part')
                return redirect(request.url)
           file = request.files['file']

           if file.filename == '':
               flash('file must have file name')
               return redirect(request.url)
           
           if not allowed_file(file.filename): # calls allow_file() to check if extension is valid
               flash('File extension not allowed')
               return redirect(request.url)

           if file  and allowed_file(file.filename): 
               filename = secure_filename(file.filename) #secure filename
               
               with open('./app/cc_fraud_model.pkl', 'rb') as file_to_pred:
                   model = pickle.load(file_to_pred) 
                   df = pd.read_csv(file)
                   predictions = model.predict(df)
                   proba_pred = model.predict_proba(df)
                   flash('Here is your predictions: ',predictions)
                   #print('The probability of the predictions is: ', proba_pred)
                   
                   # assign value to outcome of predictions 1==fraud and 0== nonfraud
                   frd ='fraud'
                   nonfrd ='Non fraud'
                   while True:
                    for pred in predictions:
                      if pred ==1:
                        frd
                      else:
                        nonfrd 
                    file.save(os.path.join(app.config['UPLOADS'],filename)) # saves file to upload folder   
                    os.remove(os.path.join(app.config['UPLOADS'], filename)) # remove file from server after making prediction
                    return render_template('public/upload_file.html', frd=frd, nonfrd=nonfrd,predictions=predictions)#, proba_pred=proba_pred)   

    return render_template('public/upload_file.html')