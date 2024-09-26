import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from PIL import Image
from datetime import datetime, date
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Setting page configuration
st.set_page_config(page_title="Customer Segmentation ", page_icon="✈️", layout='wide')

# Loading data
# df = pd.read_csv('cleaned_df.csv')

with st.sidebar:

    st.sidebar.image('Customer-Segmentation.png')
    st.sidebar.subheader("This dashboard for Indian Aviation Flights Fare aimed at predicting the prices of flight tickets")
    st.sidebar.write("")
    
    
