import streamlit as st
import pickle
import numpy as np

# Simple model load karo
model = pickle.load(open('churn_model_simple.pkl', 'rb'))

st.title("Customer Churn Predictor 🎯")

account_length = st.number_input("Account Length", min_value=0)
total_charge = st.number_input("Total Charge", min_value=0.0)
customer_service_calls = st.number_input("Customer Service Calls", min_value=0)

if st.button("Predict"):
    input_data = np.array([[account_length, total_charge, customer_service_calls]])
    result = model.predict(input_data)
    
    if result[0] == 1:
        st.error("Customer Will Churn! 🚨")
    else:
        st.success("Customer Will Stay! ✅")