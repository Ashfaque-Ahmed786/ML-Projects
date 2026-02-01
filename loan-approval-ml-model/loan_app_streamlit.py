import streamlit as st
import pickle
import numpy as np

# ---------------------------
# Background Image
def set_background(image_path):
    import base64
    with open(image_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
        }}
        .card {{
            background: rgba(0,0,0,0.65);
            padding: 30px;
            border-radius: 18px;
            max-width: 900px;
            margin: auto;
            color: white;
        }}
        label {{
            font-weight: bold !important;
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Background path (KEEP SAME)
set_background(r"C:\Users\Hp\OneDrive\Desktop\Loan approval ML project\d93aa9ae-d099-49f7-9e12-664258c75205.png")

# ---------------------------
# Load Model & Scaler
with open("loan_rf_model.pkl", "rb") as f:
    rf = pickle.load(f)

with open("loan_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ---------------------------
# UI
st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("🏦 Loan Approval Prediction")
st.write("Fill correct applicant details")

col1, col2 = st.columns(2)

with col1:
    dependents = st.number_input("Number of Dependents", min_value=0)
    income = st.number_input("Annual Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Term (Years)", min_value=0)
    cibil = st.number_input("CIBIL Score", min_value=0)

with col2:
    res_asset = st.number_input("Residential Asset Value", min_value=0)
    com_asset = st.number_input("Commercial Asset Value", min_value=0)
    lux_asset = st.number_input("Luxury Asset Value", min_value=0)
    bank_asset = st.number_input("Bank Asset Value", min_value=0)
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    employed = st.selectbox("Self Employed", ["Yes", "No"])

# ---------------------------
# Prediction
if st.button("Predict Loan Status"):

    # 🚨 RULE-BASED VALIDATION (CRITICAL)
    if (
        income <= 0 or
        loan_amount <= 0 or
        loan_term <= 0 or
        cibil < 300 or
        cibil > 900
    ):
        st.markdown(
            """
            <div style="background:#ff4d4d;padding:15px;border-radius:10px;
            font-size:22px;font-weight:bold;text-align:center;">
            ❌ Loan Rejected (Invalid Applicant Data)
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        edu = 1 if education == "Graduate" else 0
        emp = 1 if employed == "Yes" else 0

        numeric = [
            dependents, income, loan_amount, loan_term,
            cibil, res_asset, com_asset, lux_asset, bank_asset
        ]

        scaled = scaler.transform([numeric])
        final_input = np.concatenate([scaled[0], [edu, emp]])

        proba = rf.predict_proba([final_input])[0][1]
        threshold = 0.65   # STRICT approval

        if proba >= threshold:
            st.markdown(
                f"""
                <div style="background:#2ecc71;padding:15px;border-radius:10px;
                font-size:22px;font-weight:bold;text-align:center;">
                ✅ Loan Approved<br>
                Approval Probability: {proba:.2f}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="background:#e74c3c;padding:15px;border-radius:10px;
                font-size:22px;font-weight:bold;text-align:center;">
                ❌ Loan Rejected<br>
                Approval Probability: {proba:.2f}
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown('</div>', unsafe_allow_html=True)
