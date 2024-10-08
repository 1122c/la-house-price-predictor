from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

# Load the trained model
model = joblib.load("model/la_house_price_model.pkl")

# Define the input schema
class HouseFeatures(BaseModel):
    GrLivArea: float
    TotalBsmtSF: float
    OverallQual: int
    YearBuilt: int
    LotArea: float

# Define the predict endpoint
@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Extract the input data as a list
    data = [[features.GrLivArea, features.TotalBsmtSF, features.OverallQual, features.YearBuilt, features.LotArea]]
    
    # Make prediction using the trained model
    prediction = model.predict(data)
    
    # Return the prediction as a response
    return {"predicted_price": prediction[0]}
