# Manufacturing Predictive API
# Manufacturing Predictive API

This project implements a simple RESTful API for predictive analysis in manufacturing operations. The API predicts machine downtime based on features like temperature and run time using a machine learning model.

## Project Overview

The API allows users to:
- Upload a CSV file containing manufacturing data.
- Train a predictive model on the uploaded dataset.
- Make predictions on machine downtime based on input features like temperature and run time.

## Technologies Used
- Python
- FastAPI for creating the RESTful API
- scikit-learn for the machine learning model
- Uvicorn for running the FastAPI app
- Pandas for data manipulation
- Postman for testing the endpoints

## Endpoints

### 1. Upload Dataset
- **URL**: `/upload`
- **Method**: `POST`
- **Description**: Upload a CSV file containing manufacturing data (e.g., `Machine_ID`, `Temperature`, `Run_Time`, `Downtime_Flag`).
- **Request Body**: Form data with the key `file` (upload a `.csv` file).
- **Response**:
  ```json
  {
    "message": "File uploaded successfully",
    "columns": ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"]
  }

2. Train Model

    URL: /train
    Method: POST
    Description: Train the machine learning model using the uploaded dataset.
    Response:

    {
      "message": "Model trained successfully",
      "metrics": {
        "accuracy": 0.85,
        "f1_score": 0.80
      }
    }

3. Predict Downtime

    URL: /predict
    Method: POST
    Description: Predict machine downtime based on provided features like temperature and run time.
    Request Body:

{
  "Temperature": 80,
  "Run_Time": 120
}

Response:

    {
      "Downtime": "Yes",
      "Confidence": 0.85
    }

How to Run the API
Prerequisites

Make sure you have Python 3.8+ installed. You also need to install the required dependencies.

    Clone this repository to your local machine:

git clone https://github.com/yourusername/manufacturing-predictive-api.git
cd manufacturing-predictive-api

Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Run the FastAPI application:

    uvicorn app.main:app --reload

    The API will be running at http://127.0.0.1:8000.

Testing the API

You can test the API using Postman by sending POST requests to the endpoints with appropriate data.
Sample Dataset

A sample dataset (manufacturing_data.csv) has been provided. You can use it to upload and train the model.
Evaluation Metrics

The model's performance is evaluated using:

    Accuracy: The proportion of correctly predicted downtime flags.
    F1-Score: The balance between precision and recall.

Predictive Analysis for Manufacturing
 0.1.0 
OAS 3.1
/openapi.json
default


POST
/upload
Upload File


POST
/train
Train


POST
/predict
Make Prediction


GET
/
Root


Schemas
Body_upload_file_upload_postExpand allobject
HTTPValidationErrorExpand allobject
ValidationErrorExpand allobject
