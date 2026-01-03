import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model/customer_churn_decision_tree.pkl")

st.title("Customer Churn Prediction")
st.write("Decision Tree Model")

st.markdown("### Enter Customer Details")

# INPUT FIELDS 

gender = st.selectbox("Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["No", "Yes"])
Dependents = st.selectbox("Dependents", ["No", "Yes"])
tenure = st.number_input("Tenure (Months)", min_value=0)

PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

# LABEL ENCODING 

gender = 0 if gender == "Female" else 1
Partner = 0 if Partner == "No" else 1
Dependents = 0 if Dependents == "No" else 1
PhoneService = 0 if PhoneService == "No" else 1
PaperlessBilling = 0 if PaperlessBilling == "No" else 1

MultipleLines = {"No": 0, "No phone service": 1, "Yes": 2}[MultipleLines]
InternetService = {"DSL": 0, "Fiber optic": 1, "No": 2}[InternetService]

OnlineSecurity = {"No": 0, "No internet service": 1, "Yes": 2}[OnlineSecurity]
OnlineBackup = {"No": 0, "No internet service": 1, "Yes": 2}[OnlineBackup]
DeviceProtection = {"No": 0, "No internet service": 1, "Yes": 2}[DeviceProtection]
TechSupport = {"No": 0, "No internet service": 1, "Yes": 2}[TechSupport]
StreamingTV = {"No": 0, "No internet service": 1, "Yes": 2}[StreamingTV]
StreamingMovies = {"No": 0, "No internet service": 1, "Yes": 2}[StreamingMovies]

Contract = {"Month-to-month": 0, "One year": 1, "Two year": 2}[Contract]

PaymentMethod = {
    "Bank transfer (automatic)": 0,
    "Credit card (automatic)": 1,
    "Electronic check": 2,
    "Mailed check": 3
}[PaymentMethod]

# PREDICTION 

if st.button("Predict Churn"):
    input_data = np.array([[ 
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")
