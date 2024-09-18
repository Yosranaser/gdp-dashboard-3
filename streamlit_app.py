import streamlit as st
import pandas as pd

# Display header
st.header('File Upload')

# File uploader to upload dataset
file = st.file_uploader('Upload dataset', type=['csv'])

if file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(file)
    
    # Slider to choose the number of rows
    num_row = st.slider('Choose number of rows', min_value=1, max_value=len(df), step=1)
    
    # Multiselect to choose columns
    columns = st.multiselect('Choose the columns', df.columns.to_list())  # Fixed the typo here
    
    # Display the selected rows and columns
    st.write(df[columns].head(num_row))  # Display only selected columns and rows
    if columns:
        st.write(df[:num_row][columns])
    else
        st.write(df[:num_row])


 
 

