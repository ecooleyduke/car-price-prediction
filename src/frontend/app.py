import streamlit as st
import requests

API_URL = "https://car-price-api-amd-881281483784.europe-west1.run.app/predict"

st.title("Car Price Predictor")
Brand = st.text_input("Brand")
Model = st.text_input("Model")
Year = st.number_input("Year", 1990, 2025)
Mileage = st.number_input("Mileage", 0)
Fuel_Type = st.text_input("Fuel Type")
Transmission = st.text_input("Transmission")
Condition = st.text_input("Condition")

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

