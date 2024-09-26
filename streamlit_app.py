import streamlit as st
import pickle
import pandas as pd

# تحميل النموذج من الملف
def load_model():
    with open('kmeans_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# واجهة Streamlit
st.title("KMeans Model Predictor")

# تحميل النموذج
model = load_model()
st.write("Model loaded successfully!")

# رفع البيانات من المستخدم
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # قراءة البيانات
    data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')  # or 'latin1'
    st.write("Data preview:")
    st.write(data.head())
    
    # توقع الفئات باستخدام النموذج
    predictions = model.predict(data)
    
    # عرض النتائج
    st.write("Predictions:")
    st.write(predictions)
    
   
