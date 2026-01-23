import streamlit as st
import joblib
import numpy as np

model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Amount Prediction")

married = st.selectbox("Married", [0, 1])
education = st.selectbox("Education", [0, 1])
self_employed = st.selectbox("Self Employed", [0, 1])
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
income = st.number_input("Total Income", min_value=0)

if st.button("Predict"):
    data = np.array([[married, education, self_employed, dependents, income]])
    result = model.predict(data)
    st.success(f"Predicted Loan Amount: {round(result[0], 2)}")
