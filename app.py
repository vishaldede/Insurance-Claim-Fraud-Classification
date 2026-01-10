# Load Model
import joblib
import streamlit as st
import pandas as pd

model = joblib.load('insurance_fraud_model.pkl')

st.title("🕵️ Insurance Claim Fraud Prediction App")
st.write("Enter policy and claim details to predict whether the claim is fraud or genuine.")

# Input fields
policy_state = st.selectbox("Policy State", ['CA', 'NY', 'TX', 'FL', 'PA', 'IL', 'OH'])
insured_sex = st.selectbox("Insured Sex", ['Male', 'Female', 'Unknown'])
incident_severity = st.selectbox("Incident Severity", ['Trivial', 'Minor', 'Major', 'Total Loss'])
policy_deductible = st.slider("Policy Deductible", 500, 2000, 1000, 500)
vehicle_claim_amount = st.number_input("Vehicle Claim_Amount", 200, 20000, 2500)
vehicle_age = st.slider("Vehicle Age", 1, 20, 5)
num_of_claims = st.slider("Num Of Claims", 0, 10, 1)
customer_tenure = st.slider("Customer Tenure", 1, 10, 5)

# Dataframe
input_df = pd.DataFrame({
    'Policy_State': [policy_state],
    'Insured_Sex': [insured_sex],
    'Incident_Severity': [incident_severity],
    'Policy_Deductible': [policy_deductible],
    'Vehicle_Claim_Amount': [vehicle_claim_amount],
    'Vehicle_Age': [vehicle_age],
    'Num_Of_Claims': [num_of_claims],
    'Customer_Tenure': [customer_tenure]
})

# Predict
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✅ Genuine Claim")
