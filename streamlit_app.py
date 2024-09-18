import streamlit as st
import pandas as pd
import plotly.express as px

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
    columns = st.multiselect('Choose the columns', df.columns.to_list())
    
    # Display the selected rows and columns
    if columns:
        st.write(df[columns].head(num_row))
    else:
        st.write(df.head(num_row))
    
    # Create and display the Plotly scatter plot if the required columns are present
    if 'population' in df.columns and 'total_rooms' in df.columns:
        fig = px.scatter(df, x='population', y='total_rooms')
        st.plotly_chart(fig)
    else:
        st.write("The dataset does not contain the required columns for the scatter plot.")

 
 

