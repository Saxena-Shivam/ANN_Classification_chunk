import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle
import os

# Load files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "regression_model.h5")
encoder_path = os.path.join(BASE_DIR, "label_encoder_gender.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

# Load model
model = tf.keras.models.load_model(model_path, compile=False)

# Load encoder and scaler
with open(encoder_path, "rb") as file:
    label_encoder_gender = pickle.load(file)

with open(scaler_path, "rb") as file:
    scaler = pickle.load(file)

# Streamlit UI
st.title("Customer Salary Prediction")

st.write("Enter customer details to predict salary")

# Inputs
credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

age = st.slider(
    "Age",
    18,
    92,
    35
)

tenure = st.slider(
    "Tenure",
    0,
    10,
    5
)

balance = st.number_input(
    "Balance",
    min_value=0.0,
    value=0.0
)

num_of_products = st.slider(
    "Number Of Products",
    1,
    4,
    1
)

has_cr_card = st.selectbox(
    "Has Credit Card",
    [0, 1]
)

is_active_member = st.selectbox(
    "Is Active Member",
    [0, 1]
)

exited = st.selectbox(
    "Exited",
    [0, 1]
)

# Geography Encoding
geo_france = 1 if geography == "France" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# Gender Encoding
gender_encoded = label_encoder_gender.transform([gender])[0]

# Input Data
input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [gender_encoded],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    "Exited": [exited],
    "Geography_France": [geo_france],
    "Geography_Germany": [geo_germany],
    "Geography_Spain": [geo_spain]
})

# Ensure same column order as training
input_data = input_data[scaler.feature_names_in_]

# Scale
input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict Salary"):
    prediction = model.predict(input_scaled, verbose=0)

    predicted_salary = float(prediction[0][0])

    st.success(
        f"Predicted Salary: ₹{predicted_salary:,.2f}"
    )