import streamlit as st
import pandas as pd
st.header('file uplaod')
file=st.file_uploader('upload dataset',type=['csv'])
if file is not None:
 df=pd.read_csv(file)
 st.write(df)
 

