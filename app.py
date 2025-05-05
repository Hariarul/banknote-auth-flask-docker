from flask import Flask,request
import numpy as np
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

from joblib import load
model = load("bank_classifier.pkl")

@app.route('/')
def use():
    return "Hi hari"

@app.route("/predict")
def bank_note_authentication():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance = float(request.args.get('variance'))
    skewness = float(request.args.get('skewness'))
    curtosis = float(request.args.get('curtosis'))
    entropy = float(request.args.get('entropy'))
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    return "predicted value is:"+ str(prediction)

@app.route("/predict_file",methods=['POST'])
def bank_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df = pd.read_csv(request.files.get('file'))

    prediction = model.predict(df)
    return "predicted value is:"+ str(list(prediction))


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5002)
