import streamlit as st
import requests

API_URL = "https://car-price-api-amd-881281483784.europe-west1.run.app/predict"

# Categorical options
BRANDS = ["Toyota", "Honda", "Suzuki", "Ford", "BMW", "Mercedes"]
FUEL_TYPES = ["Petrol", "Diesel", "Hybrid", "Electric"]
TRANSMISSIONS = ["Manual", "Automatic"]
CONDITIONS = ["New", "Used", "Excellent", "Good", "Fair"]

# User Inputs
Brand = st.selectbox("Brand", BRANDS)
Model = st.text_input("Model")  # Free text, as models vary a lot
Year = st.number_input("Year", min_value=1990, max_value=2025, value=2020)
Mileage = st.number_input("Mileage", min_value=0, step=1000)
Fuel_Type = st.selectbox("Fuel Type", FUEL_TYPES)
Transmission = st.selectbox("Transmission", TRANSMISSIONS)
Condition = st.selectbox("Condition", CONDITIONS)

if st.button("Predict"):
    payload = {
        "Brand": Brand,
        "Model": Model,
        "Year": Year,
        "Mileage": Mileage,
        "Fuel_Type": Fuel_Type,
        "Transmission": Transmission,
        "Condition": Condition
    }
    response = requests.post(API_URL, json=payload)
    st.write("Predicted Price:", "$" + str(round(response.json()["predicted_price"], 2)))

