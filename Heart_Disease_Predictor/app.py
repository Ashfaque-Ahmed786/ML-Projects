import streamlit as st
import numpy as np
import pickle
from PIL import Image

# ---------- Load Model and Scaler ----------
with open("rf.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler (3).pkl", "rb") as f:
    scaler = pickle.load(f)

# ---------- Page Config ----------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
}
h1 {
    color: #e63946;
}
.stButton>button {
    background-color: #1d3557;
    color: white;
    height: 3em;
    width: 100%;
    border-radius: 10px;
    font-size: 18px;
}
.stTextInput>div>input {
    height: 2.5em;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("🫀 Heart Disease Prediction")
st.markdown("Enter the patient details below to predict the risk of heart disease.")

# ---------- Columns Layout ----------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 20, 100, 40)
    sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x==0 else "Male")
    chest_pain_type = st.selectbox("Chest Pain Type (1-4)", [1, 2, 3, 4])
    resting_bp_s = st.number_input("Resting Blood Pressure", 80, 200, 120)

with col2:
    cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 400, 200)
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    resting_ecg = st.selectbox("Resting ECG (0-2)", [0, 1, 2])
    max_heart_rate = st.number_input("Max Heart Rate", 60, 220, 150)

with col3:
    exercise_angina = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope (1-3)", [1, 2, 3])

st.markdown("---")  # Horizontal line

# ---------- Predict Button ----------
if st.button("🔍 Predict"):
    # Prepare input data
    input_data = np.array([[age, sex, chest_pain_type, resting_bp_s, cholesterol,
                            fasting_blood_sugar, resting_ecg, max_heart_rate,
                            exercise_angina, oldpeak, st_slope]])
    
    # Scale numerical features
    numerical_indices = [0, 3, 4, 7, 9]
    input_data[:, numerical_indices] = scaler.transform(input_data[:, numerical_indices])

    # Make prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)[0][1]

    # Display results
    if prediction[0] == 1:
        st.error(f"⚠️ Heart Disease Detected! Risk Probability: {prediction_proba*100:.2f}%")
    else:
        st.success(f"✅ No Heart Disease Detected! Risk Probability: {prediction_proba*100:.2f}%")

# ---------- Footer ----------
st.markdown("""
---
#### Developed by ASHFAQUE AHMED 🧑‍💻 | Machine Learning Project
""")
