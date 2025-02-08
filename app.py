import streamlit as st
import pickle
import numpy as np
import pandas as pd

from PIL import Image 



# Assuming you have a trained model

import requests
import io

url = "https://raw.githubusercontent.com/harthej/Solar_power_generation_forecasting/main/gradient_boosting_model.pkl"

response = requests.get(url)

if response.status_code == 200:
    try:
        file = io.BytesIO(response.content)
        model = pickle.load(file)
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading model: {e}")
else:
    st.error(f"Failed to download the file. Status code: {response.status_code}")
# Streamlit app
st.title("Solar Power Prediction App")

st.write("""
This app predicts the **power generated** by solar panels based on input features.
""")

# Define input fields for features
st.sidebar.header("Input Features")

def user_input_features():
    feature1 = st.sidebar.number_input("Feature 1:distance-to-solar-noon", value=0.397172237)
    feature2 = st.sidebar.number_input("Feature 2:temperature", value=69)
    feature3 = st.sidebar.number_input("Feature 3:wind-direction", value=28)
    feature4 = st.sidebar.number_input("Feature 4:wind-speed",value=7.5)
    feature5 = st.sidebar.number_input("Feature 5:sky-cover", value=0)
    feature6 = st.sidebar.number_input("Feature 6:visibility", value=10)
    feature7 = st.sidebar.number_input("Feature 7:Humidity", value=70)
    feature8 = st.sidebar.number_input("Feature 8:average-wind-speed-(period)", value=0)
    feature9 = st.sidebar.number_input("Feature 9:average-pressure-(period)", value=29.89)
    data = {
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3,
        'feature4': feature4,
        'feature5': feature5,
        'feature6': feature6,
        'feature7': feature7,
        'feature8': feature8,
        'feature9': feature9,
    }
    return np.array([list(data.values())])


# Collect user input
input_data = user_input_features()

# Prediction
if model is None:
    st.error("Model is not loaded. Check if the model is being loaded correctly.")

if st.button("Predict Power Generated"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Power Generated: {prediction[0]:.2f} kW")

st.write("Adjust the input values in the sidebar to see the predictions.")
