# Bank Note Authentication API

This is a Flask-based API that predicts the authenticity of bank notes using a machine learning model. It supports both single data point prediction via query parameters and batch prediction via CSV file upload.

---

## Features

- Predict using variance, skewness, curtosis, and entropy
- Accepts both individual inputs and CSV files
- Swagger UI documentation for easy testing
- Ready for containerization with Docker

---

## Project Structure

.
├── app.py                # Main Flask application  
├── bank_classifier.pkl   # Trained ML model  
├── requirements.txt      # Python dependencies  
├── Dockerfile            # For containerization  
└── README.md             # Project description

---

## Requirements

- Python 3.9
- pip

Install dependencies:
pip install -r requirements.txt

Run Locally
python app.py

Predict Using URL Params
GET /predict?variance=2.3&skewness=4.5&curtosis=1.2&entropy=0.4

Predict Using CSV Upload
Endpoint: /predict_file
Method: POST
Form-Data:
variance,skewness,curtosis,entropy

Swagger UI
Visit http://localhost:5000/apidocs to use Swagger interface.

Docker 
docker build -t banknote-api .
docker run -p 5000:5000 banknote-api

