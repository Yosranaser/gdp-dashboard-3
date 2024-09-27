import streamlit as st
import pickle
import pandas as pd

# Load the KMeans model from a file
def load_model():
    with open('kmeans_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Streamlit interface
st.title("KMeans Model Predictor")

# Load the model
model = load_model()
st.write("Model loaded successfully!")

# File uploader for the user to upload a CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded data
    data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')  # Adjust encoding if needed
    st.write("Data preview:")
    st.write(data.head())

    
