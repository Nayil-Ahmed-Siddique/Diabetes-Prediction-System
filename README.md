# Diabetes Prediction Using Machine Learning
 Data Science Capstone Project To Build a model to accurately predict whether the patients in the dataset have diabetes or not? Using Python and Tableau 10

## Deployment

This model is deployed as a REST API using FastAPI.

### Endpoints
- `/predict` → returns diabetes prediction

### Tech Stack
- FastAPI
- Railway

### Live API
<your link>

This model was deployed as a REST API using FastAPI and Railway.

(The live service was stopped to avoid resource usage)
# Problem Statement


NIDDK (National Institute of Diabetes and Digestive and Kidney Diseases) research creates knowledge about and treatments for the most chronic, costly, and consequential diseases.
The dataset used in this project is originally from NIDDK. The objective is to predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset.
Build a model to accurately predict whether the patients in the dataset have diabetes or not.
![81200287-93500880-8fe5-11ea-8669-f3985d445923](https://user-images.githubusercontent.com/110838853/192422423-dea8e137-d476-4b4c-9c57-b93e47e445c5.png)

# Dataset Description
The datasets consists of several medical predictor variables and one target variable (Outcome). Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and more.

 

Variables	Description
Pregnancies	Number of times pregnant
Glucose	Plasma glucose concentration in an oral glucose tolerance test
BloodPressure	Diastolic blood pressure (mm Hg)
SkinThickness	Triceps skinfold thickness (mm)
Insulin	Two hour serum insulin
BMI	Body Mass Index
DiabetesPedigreeFunction	Diabetes pedigree function
Age	Age in years
Outcome	Class variable (either 0 or 1). 268 of 768 values are 1, and the others are 0


# 🩺 Diabetes Prediction API — ML Deployment System

A production-style machine learning API built using FastAPI for real-time diabetes prediction.  
This project demonstrates end-to-end ML workflow including model training, API development, cloud deployment, and CI/CD integration.

---

## ✨ What this project does

- Predicts diabetes likelihood based on medical input features
- Exposes model via REST API (FastAPI)
- Supports real-time prediction via HTTP endpoints
- Includes automated testing and CI/CD pipeline (GitHub Actions)
- Deployed on cloud (Railway)

---

## 🌐 Live API

Base URL:
https://your-api-url.up.railway.app

Swagger Docs:
https://your-api-url.up.railway.app/docs

---

## 📁 Project Structure

Diabetes-Prediction-System/
├── main.py                 # FastAPI application
├── train_model.py         # Model training script
├── model.pkl              # Trained ML model
├── requirements.txt       # Dependencies
├── test_app.py            # API test cases
├── Procfile               # Deployment config
└── README.md

---

## ⚙️ Tech Stack

- Python
- Scikit-learn
- FastAPI
- Uvicorn
- GitHub Actions (CI/CD)
- Railway (Deployment)

---

## 🚀 Running Locally

### 1. Create virtual environment

python -m venv venv

### Activate

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Run API

uvicorn main:app --reload

---

### 4. Open in browser

http://127.0.0.1:8000/docs

---

## 📡 API Usage

### Endpoint

POST /predict

### Sample Request

```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 125,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

### Sample Response

```json
{
  "prediction": 1
}
```

---

## 🧪 Testing

Run tests locally:

pytest

CI pipeline automatically:
- installs dependencies
- runs tests
- validates API functionality

---

## 🔄 CI/CD Pipeline

Implemented using GitHub Actions:

- Triggered on push to main branch
- Runs automated tests
- Validates API endpoints
- Includes deployment stage (extendable)

---

## ☁️ Deployment

Deployed on Railway for live API access.

Supports:
- auto-redeploy on code updates
- public endpoint exposure

---

## 🧠 Key Learnings

- Building end-to-end ML systems
- Converting models into APIs
- Real-time inference serving
- CI/CD integration for ML workflows
- Cloud deployment of ML services

---

## 📌 Future Improvements

- Model versioning
- Input validation enhancements
- Docker containerization
- Monitoring & logging
- Scalable deployment (AWS/GCP)

---

## 📜 License

For educational and demonstration purposes.

---

## 🧑‍💻 Author

Built to demonstrate practical ML deployment and system design skills.
