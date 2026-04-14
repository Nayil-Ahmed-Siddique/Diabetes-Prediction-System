# -----------------------------
# 1. Create API
# -----------------------------
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# -----------------------------
# 2. Load Model
# -----------------------------
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


# -----------------------------
# 3. Input Schema (VERY IMPORTANT)
# -----------------------------
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# -----------------------------
# 4. Routes
# -----------------------------
@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running"}


@app.post("/predict")
def predict(data: PatientData):

    # Convert structured input → model format
    input_data = [[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]]

    prediction = model.predict(input_data)

    return {"prediction": int(prediction[0])}