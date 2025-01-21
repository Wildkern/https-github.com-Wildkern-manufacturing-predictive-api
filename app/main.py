from fastapi import FastAPI
from app.routes.endpoints import router

app = FastAPI(title="Predictive Analysis for Manufacturing")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Predictive Analysis API for Manufacturing!"}
