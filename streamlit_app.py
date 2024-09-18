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
    
    # Filter only numeric columns for plotting
    numeric_columns = df.select_dtypes(include='number').columns.to_list()
    
    # Create 3 columns in the Streamlit layout
    col1, col2, col3 = st.columns(3)
    
    # Select the x-axis, y-axis, and color columns
    with col1:
        x_col = st.selectbox('Choose X-axis', numeric_columns)
    
    with col2:
        y_col = st.selectbox('Choose Y-axis', numeric_columns)
    
    with col3:
        color = st.selectbox('Choose Color', df.columns.to_list())
    
    # Create and display the scatter plot using Plotly
    fig = px.scatter(df, x=x_col, y=y_col, color=color)
    st.plotly_chart(fig)

