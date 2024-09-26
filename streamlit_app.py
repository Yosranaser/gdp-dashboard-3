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

    # Ensure data only contains numeric columns
    numeric_data = data.select_dtypes(include=['float64', 'int64'])

    # Check if numeric data is available
    if numeric_data.empty:
        st.error("The uploaded file doesn't contain any numeric columns.")
    else:
        # Predictions using the model
        predictions = model.predict(numeric_data)
        
        # Display predictions
        st.write("Predictions:")
        st.write(predictions)
        
        # Create a DataFrame for results
        result_df = pd.DataFrame(predictions, columns=["Cluster"])
        result_df['Original Data'] = data.values.tolist()  # Include original data with predictions
        
        # Convert results to CSV for download
        csv_result = result_df.to_csv(index=False)
        
        # Download button for the user to download predictions
        st.download_button(
            label="Download Predictions as CSV",
            data=csv_result,
            file_name="predictions.csv",
            mime="text/csv",
        )
