import os
import joblib
import pandas as pd


# ============================================================
# MODEL PATH
# ============================================================

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "severity_pipeline.pkl"
)


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(MODEL_PATH)


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_severity(patient_data):

    # Convert input dictionary into DataFrame
    patient_df = pd.DataFrame([patient_data])

    # Predict severity
    prediction = model.predict(patient_df)[0]

    # Get probabilities
    probabilities = model.predict_proba(patient_df)[0]

    # Get class names
    classes = model.classes_

    # Find probability of predicted class
    predicted_index = list(classes).index(prediction)

    confidence = probabilities[predicted_index]

    return {
        "severity": prediction,
        "confidence": round(float(confidence), 4)
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    patient = {
        "Age": 65,
        "Gender": "Male",
        "Symptom_1": "Fever",
        "Symptom_2": "Cough",
        "Symptom_3": "Breathlessness",
        "Heart_Rate_bpm": 110,
        "Body_Temperature_C": 39.2,
        "Oxygen_Saturation_%": 88,
        "Systolic_BP": 90,
        "Diastolic_BP": 60
    }

    result = predict_severity(patient)

    print(result)