# Customer-Churn-Prediction Decision Tree Model
1. Project Overview

This project predicts whether a customer is likely to churn (leave a service) using Machine Learning.
A Decision Tree classifier is trained on a telecom customer dataset, and a simple Streamlit-based UI is used to make predictions based on customer details.

2. Dataset Source

Name: Telco Customer Churn Dataset
Source: Kaggle (Telecom Customer Churn)

Description:
The dataset contains customer demographic information, services subscribed, billing details, and a target column (Churn) indicating whether the customer left the service.

3. Steps to run the project

Step 1: Install Dependencies pip install -r requirements.txt

Step 2: Run the Streamlit Application streamlit run app.py

4. Model Used

Algorithm: Decision Tree Classifier
Reason: Decision Trees are easy to understand and interpret, making them suitable for beginner-level classification problems.

5. Final Result Summary 

The trained Decision Tree model can predict customer churn effectively.

Output interpretation:
0 → Customer will NOT churn
1 → Customer WILL churn
Model Evaluation : Accuracy - 0.725

