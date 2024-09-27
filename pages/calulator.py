import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the KMeans model
with open('kmeans_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# Streamlit layout
st.title("ATM Services Dashboard")

# File uploader for the dataset
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    col1, col2, col3 = st.columns(3)

    # Plot 1: Cluster vs Feature1
    with col1:
        st.header("Cluster vs Feature1")
        plt.figure(figsize=(5, 4))
        sns.scatterplot(x=data['lat'], y=data['lng'], hue=kmeans_model.labels_, palette='viridis')
        plt.title('Location Clusters')
        st.pyplot(plt)

    # Plot 2: Services Distribution
    with col2:
        st.header("Services Distribution")
        plt.figure(figsize=(5, 4))
        service_counts = data['services'].value_counts()
        sns.barplot(x=service_counts.index, y=service_counts.values)
        plt.xticks(rotation=90)
        plt.title('Distribution of Services')
        st.pyplot(plt)

    # Plot 3: Clusters by Area
    with col3:
        st.header("Clusters by Area")
        plt.figure(figsize=(5, 4))
        sns.countplot(x=kmeans_model.labels_, data=data)
        plt.title('Number of ATMs per Cluster')
        st.pyplot(plt)
else:
    st.warning("Please upload a CSV file.")
