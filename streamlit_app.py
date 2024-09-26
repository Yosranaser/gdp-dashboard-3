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
    result_df = pd.DataFrame(predictions, columns=["Cluster"])
    result_df['Data'] = data.values.tolist()  # حفظ البيانات الأصلية مع التوقعات
    csv_result = result_df.to_csv(index=False)
    
    st.download_button(
        label="Download Predictions as CSV",
        data=csv_result,
        file_name="predictions.csv",
        mime="text/csv",
    )
#with open('your_script.py', 'r', encoding='utf-8') as file:
   # content = file.read()
with open('your_script_clean.py', 'w', encoding='utf-8') as file:
    file.write(content)
file_path = 'streamlit_app.py'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Replace non-breaking space with a regular space
cleaned_content = content.replace('\u00A0', ' ')

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_content)

print("Non-breaking spaces removed successfully!")

# Replace non-breaking spaces with normal spaces
content = content.replace('\u00A0', ' ')


