from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

# Placeholder for model loading
# model = joblib.load("la_house_price_model.pkl")

class HouseFeatures(BaseModel):
    GrLivArea: float
    TotalBsmtSF: float
    OverallQual: int
    YearBuilt: int
    LotArea: float

@app.post("/predict")
def predict_price(features: HouseFeatures):
    data = [[features.GrLivArea, features.TotalBsmtSF, features.OverallQual, features.YearBuilt, features.LotArea]]
    # Placeholder for prediction logic
    # prediction = model.predict(data)
    # return {"predicted_price": prediction[0]}
    return {"message": "Model not loaded"}
