# Medical Severity Prediction

A machine learning-based web application that predicts a patient's **severity level** as **Mild, Moderate, or Severe** using patient information, symptoms, and vital signs.

> **Note:** This project is intended for educational and demonstration purposes. It is not a medical diagnosis system and should not be used for real-world clinical decisions.

---

## 📌 Project Overview

The goal of this project is to build a supervised machine learning classification model that predicts the severity of a patient's condition based on:

* Age
* Gender
* Symptoms
* Heart Rate
* Body Temperature
* Oxygen Saturation
* Systolic Blood Pressure
* Diastolic Blood Pressure

The original dataset contains additional columns such as `Patient_ID`, `Diagnosis`, and `Treatment_Plan`. These columns are intentionally removed during data cleaning to prevent them from being used as model features.

---

## 🎯 Target Variable

The model predicts three severity classes:

```text
Mild
Moderate
Severe
```

This is a **multi-class classification problem**.

---

## 🗂️ Project Structure

```text
severity-prediction/
│
├── data/
│   └── severity_dataset.csv
│
├── notebooks/
│   └── severity_prediction.ipynb
│
├── models/
│   └── severity_pipeline.pkl
│
├── src/
│   └── predict.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder/File Description

| File/Folder            | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| `data/`                | Contains the dataset                                          |
| `notebooks/`           | Contains EDA, preprocessing, training and evaluation notebook |
| `models/`              | Stores the trained ML pipeline                                |
| `src/predict.py`       | Loads the trained model and performs predictions              |
| `templates/index.html` | Frontend HTML page                                            |
| `static/style.css`     | Frontend styling                                              |
| `app.py`               | Flask web application                                         |
| `requirements.txt`     | Python dependencies                                           |
| `README.md`            | Project documentation                                         |

---

## 🔄 Machine Learning Workflow

The project follows this workflow:

```text
Dataset
   ↓
Data Inspection
   ↓
Exploratory Data Analysis
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Hyperparameter Tuning
   ↓
Final Model
   ↓
Save Pipeline
   ↓
Flask API
   ↓
Web Interface
```

---

## 🧹 Data Cleaning

The following columns are removed from the dataset:

```text
Patient_ID
Diagnosis
Treatment_Plan
```

### Why?

* `Patient_ID` is only an identifier and has no useful predictive meaning.
* `Diagnosis` is deliberately excluded because it can directly reveal information about the patient's condition.
* `Treatment_Plan` can also contain information derived from the patient's condition and may cause data leakage.

---

## 🩺 Blood Pressure Feature Engineering

The original blood pressure column has values such as:

```text
120/80
```

This is converted into two numerical features:

```text
Systolic_BP
Diastolic_BP
```

For example:

```text
120/80
 ↓
Systolic_BP = 120
Diastolic_BP = 80
```

The original `Blood_Pressure_mmHg` column is then removed.

---

## 📊 Exploratory Data Analysis

The notebook performs EDA to understand:

* Dataset shape
* Data types
* Missing values
* Duplicate records
* Severity distribution
* Numerical feature distributions
* Symptoms distribution
* Gender vs severity
* Vital signs vs severity
* Correlation between numerical variables

Visualizations include:

* Count plots
* Histograms
* Box plots
* Correlation heatmap

---

## ⚙️ Data Preprocessing

The dataset contains both numerical and categorical features.

### Numerical Features

```text
Age
Heart_Rate_bpm
Body_Temperature_C
Oxygen_Saturation_%
Systolic_BP
Diastolic_BP
```

These features are standardized using:

```python
StandardScaler()
```

### Categorical Features

```text
Gender
Symptom_1
Symptom_2
Symptom_3
```

These features are converted into numerical form using:

```python
OneHotEncoder(handle_unknown="ignore")
```

The preprocessing is implemented using a `ColumnTransformer`.

---

## 🤖 Machine Learning Models

Multiple classification algorithms are evaluated:

### 1. Logistic Regression

Used as a baseline classification model.

### 2. Random Forest

An ensemble learning algorithm that combines multiple decision trees.

### 3. Gradient Boosting

An ensemble technique that builds models sequentially to improve prediction performance.

---

## 🔧 Hyperparameter Tuning

Random Forest hyperparameters are optimized using:

```python
GridSearchCV
```

The following parameters are explored:

```python
n_estimators
max_depth
min_samples_split
min_samples_leaf
```

Five-fold cross-validation is used with:

```python
scoring="f1_weighted"
```

The best-performing configuration is then evaluated on the test dataset.

---

## 📈 Model Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report
* Confusion Matrix

Special attention is also given to the **Severe** class because correctly identifying severe cases is particularly important for this project.

---

## 💾 Model Saving

The final preprocessing and classification steps are combined into a single Scikit-learn pipeline.

The pipeline is saved using `joblib`:

```text
models/severity_pipeline.pkl
```

This allows the same preprocessing steps used during training to automatically be applied when making predictions.

---

## 🔮 Prediction

The prediction module is located at:

```text
src/predict.py
```

Example input:

```python
patient = {
    "Age": 65,
    "Gender": "Male",
    "Symptom_1": "Fever",
    "Symptom_2": "Cough",
    "Symptom_3": "Shortness of breath",
    "Heart_Rate_bpm": 110,
    "Body_Temperature_C": 39.2,
    "Oxygen_Saturation_%": 88,
    "Systolic_BP": 90,
    "Diastolic_BP": 60
}
```

The prediction function returns:

```json
{
    "severity": "Severe",
    "confidence": 0.87
}
```

The confidence represents the model's predicted probability for the selected class.

---

## 🌐 Flask Web Application

The project uses Flask to provide a web interface.

The application contains:

```text
GET /
```

for displaying the frontend and:

```text
POST /predict
```

for receiving patient information and returning the prediction.

### API Request Example

```json
{
    "Age": 65,
    "Gender": "Male",
    "Symptom_1": "Fever",
    "Symptom_2": "Cough",
    "Symptom_3": "Shortness of breath",
    "Heart_Rate_bpm": 110,
    "Body_Temperature_C": 39.2,
    "Oxygen_Saturation_%": 88,
    "Systolic_BP": 90,
    "Diastolic_BP": 60
}
```

### API Response

```json
{
    "severity": "Severe",
    "confidence": 0.87
}
```

---

## 💻 Web Interface

The frontend provides input fields for:

### Patient Information

* Age
* Gender

### Symptoms

* Symptom 1
* Symptom 2
* Symptom 3

### Vital Signs

* Heart Rate
* Body Temperature
* Oxygen Saturation
* Systolic Blood Pressure
* Diastolic Blood Pressure

After clicking **Predict Severity**, the result is displayed on the same page along with the model confidence.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd severity-prediction
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For Linux/macOS:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Train the Model

Open:

```text
notebooks/severity_prediction.ipynb
```

Run all notebook cells.

The trained pipeline will be saved to:

```text
models/severity_pipeline.pkl
```

---

### 5. Test Prediction

From the project root:

```bash
python src/predict.py
```

---

### 6. Run Flask Application

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000/
```

Open the address in your browser to use the application.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Logistic Regression
* Random Forest
* Gradient Boosting
* GridSearchCV

### Model Persistence

* Joblib

### Web Development

* Flask
* HTML
* CSS
* JavaScript

---

## 📦 Requirements

Typical dependencies include:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
flask
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🔐 Important Considerations

This project is an **educational machine learning application**.

The predictions should not be interpreted as medical diagnoses or used to make clinical decisions. Real medical applications require clinically validated datasets, appropriate medical oversight, rigorous external validation, calibration, safety testing, and compliance with applicable regulations.

---

## 👨‍💻 Author

**Shubham Kumar**

B.Tech CSE Student

---

## ⭐ Future Improvements

Possible improvements include:

* Try additional classification algorithms
* Perform more extensive hyperparameter tuning
* Handle class imbalance if present
* Add model explainability using SHAP
* Add prediction history using a database
* Add input validation
* Deploy the application online
* Monitor model performance
* Use a larger and clinically validated dataset

---

## 📄 License

This project is intended for educational and learning purposes.
