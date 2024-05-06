import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('cropapp1')

# Define the UI layout and user inputs
st.title('Crop Recommendation System')

st.write('Enter the values for Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall to get the recommended crop.')

nitrogen = st.slider('Nitrogen', min_value=0, max_value=100, value=50)
phosphorus = st.slider('Phosphorus', min_value=0, max_value=100, value=50)
potassium = st.slider('Potassium', min_value=0, max_value=100, value=50)
temperature = st.slider('Temperature', min_value=0.0, max_value=50.0, value=25.0)
humidity = st.slider('Humidity', min_value=0.0, max_value=100.0, value=50.0)
ph = st.slider('pH', min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.slider('Rainfall', min_value=0.0, max_value=500.0, value=100.0)

# Prepare the user input in the required format
user_input = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]

# Predict the crop
prediction = model.predict(user_input)

# Display the prediction
st.write('Predicted Crop:', prediction[0])
