# app.py

import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("insurance_fraud_best_model.pkl", "rb"))

st.set_page_config(page_title="Insurance Claim Fraud Detector", layout="centered")

st.title("🕵️ Insurance Claim Fraud Prediction App")
st.write("Enter policy and claim details to predict whether the claim is **fraudulent or genuine**.")

# Input fields
policy_state = st.selectbox("Policy State", ['CA', 'NY', 'TX', 'FL', 'PA', 'IL', 'OH'])
insured_sex = st.selectbox("Insured Sex", ['Male', 'Female', 'Unknown'])
incident_severity = st.selectbox("Incident Severity", ['Trivial', 'Minor', 'Major', 'Total Loss'])
policy_deductible = st.slider("Policy Deductible ($)", 500, 2000, 1000, 500)
vehicle_claim_amount = st.number_input("Vehicle Claim Amount ($)", min_value=200.0, max_value=20000.0, value=2500.0)
vehicle_age = st.slider("Vehicle Age (years)", 1, 20, 5)
num_of_claims = st.slider("Number of Past Claims", 0, 10, 1)
customer_tenure = st.slider("Customer Tenure (years)", 1, 10, 5)

# Prepare input
input_df = pd.DataFrame({
    'policy_state': [policy_state],
    'policy_deductible': [policy_deductible],
    'insured_sex': [insured_sex],
    'incident_severity': [incident_severity],
    'vehicle_claim_amount': [vehicle_claim_amount],
    'vehicle_age': [vehicle_age],
    'num_of_claims': [num_of_claims],
    'customer_tenure': [customer_tenure]
})

# Predict
if st.button("🔍 Predict Fraud"):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Fraud Detected! (Probability: {prob:.2%})")
    else:
        st.success(f"✅ Legitimate Claim (Probability of Fraud: {prob:.2%})")

st.markdown("---")
st.caption("Built by A — Junior Data Scientist Project")
