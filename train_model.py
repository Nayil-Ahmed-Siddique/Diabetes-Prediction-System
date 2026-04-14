# -----------------------------
# 1. Load Dataset
# -----------------------------
import pandas as pd

data = pd.read_csv("health care diabetes.csv")


# -----------------------------
# 2. Data Preprocessing
# -----------------------------
import numpy as np

# Columns where 0 means missing
cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Replace 0 with NaN
data[cols_with_zero] = data[cols_with_zero].replace(0, np.nan)

# Fill missing values
# Insulin → median (skewed)
data['Insulin'] = data['Insulin'].fillna(data['Insulin'].median())

# Others → mean
cols_mean = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']
data[cols_mean] = data[cols_mean].fillna(data[cols_mean].mean())


# -----------------------------
# 3. Split Features & Target
# -----------------------------
X = data.drop('Outcome', axis=1)
y = data['Outcome']


# -----------------------------
# 4. Handle Imbalance (SMOTE)
# -----------------------------
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)


# -----------------------------
# 5. Train Model
# -----------------------------
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_resampled, y_resampled)


# -----------------------------
# 6. Save Model
# -----------------------------
import pickle
                                             
with open("model.pkl", "wb") as f:           #pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")