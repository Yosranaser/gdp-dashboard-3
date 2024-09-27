import streamlit as st
import pickle
import pandas as pd
from sklearn.cluster import KMeans
import sklearn

# Print the scikit-learn version for debugging
st.write(f"scikit-learn version: {sklearn.__version__}")

# Function to load the KMeans model from a file with error handling
def load_model():
    try:
        with open('kmeans_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Make sure the 'kmeans_model.pkl' file is in the correct directory.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

# Streamlit interface
st.title("KMeans Model Predictor")
st.image("Customer-Segmentation.png", caption="Customer-Segmentation", use_column_width=True)

# Load the model
model
