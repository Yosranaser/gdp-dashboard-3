import streamlit as st
import pandas as pd
st.header('file uplaod')
file=st.file_uploader('upload dataset',type=['csv'])
if file is not None:
 df=pd.read_csv(file)
 num_row=st.slider('choose num of row',min_value=1,max_value=len(df),step=1)
 coloums=st.muliselect('choose num of name of coloums',df.coloums.to_list())
 st.write(df[:num_row][coloums])

 
 

