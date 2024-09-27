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


st.sidebar.title("Input Data")

# Taking inputs from the user in the sidebar
unit_price = st.sidebar.number_input("Enter Unit Price", min_value=0.0, step=1)
quantity = st.sidebar.number_input("Enter Quantity", min_value=0, step=1)

# Calculate total price
if unit_price and quantity:
    total_price = unit_price * quantity
    st.write(f"Total Price: {total_price}")
    
