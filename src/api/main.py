from fastapi import FastAPI
import joblib
import pandas as pd
from .schemas import CarInput

app = FastAPI(title="Car Price Prediction API")

model = joblib.load("src/models/model.pkl")

@app.get("/")
def root():
    return {"message": "Car Price Prediction API running"}

@app.post("/predict")
def predict(car: CarInput):
    data = car.model_dump()
    data["Fuel Type"] = data.pop("Fuel_Type")
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    return {"predicted_price": float(pred)}
