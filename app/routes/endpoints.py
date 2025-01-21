from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.models.model import train_model, predict
from app.utils.helpers import process_csv

router = APIRouter()

# Global variable to store the dataset and model
data = {"dataset": None, "model": None}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        data["dataset"] = process_csv(file)
        return {"message": "File uploaded successfully", "columns": list(data["dataset"].columns)}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

@router.post("/train")
async def train():
    if data["dataset"] is None:
        return JSONResponse(status_code=400, content={"error": "No dataset uploaded"})
    try:
        model, metrics = train_model(data["dataset"])
        data["model"] = model
        return {"message": "Model trained successfully", "metrics": metrics}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

@router.post("/predict")
async def make_prediction(features: dict):
    if data["model"] is None:
        return JSONResponse(status_code=400, content={"error": "No model trained"})
    try:
        prediction = predict(data["model"], features)
        return prediction
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
