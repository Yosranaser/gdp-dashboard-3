import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the KMeans model
with open('kmeans_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# Load your dataset (you can replace this with the actual dataset path)
data = pd.read_csv('/mnt/data/atm_dataset.csv')

# Streamlit layout with three columns
st.title("ATM Services Dashboard")

col1, col2, col3 = st.columns(3)

# Plot 1: First column (e.g., cluster vs feature1)
with col1:
    st.header("Cluster vs Feature1")
    plt.figure(figsize=(5, 4))
    sns.scatterplot(x=data['lat'], y=data['lng'], hue=kmeans_model.labels_, palette='viridis')
    plt.title('Location Clusters')
    st.pyplot(plt)

# Plot 2: Second column (e.g., services distribution)
with col2:
    st.header("Services Distribution")
    plt.figure(figsize=(5, 4))
    service_counts = data['services'].value_counts()
    sns.barplot(x=service_counts.index, y=service_counts.values)
    plt.xticks(rotation=90)
    plt.title('Distribution of Services')
    st.pyplot(plt)

# Plot 3: Third column (e.g., clusters in specific area)
with col3:
    st.header("Clusters by Area")
    plt.figure(figsize=(5, 4))
    sns.countplot(x=kmeans_model.labels_, data=data)
    plt.title('Number of ATMs per Cluster')
    st.pyplot(plt)
