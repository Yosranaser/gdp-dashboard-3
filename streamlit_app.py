import streamlit as st
import time
area=None
st.sidebar.title('sidebar')
st.header('calculate area')
with st.sidebar:
 choose=st.selectbox('choose box',['circle','trangle'])
if choose=='circle' :
  r=st.number_input('enter radius',min_value=1,max_value=100)
  area=3.14*r*r
elif choose=='trangle' :
  hight=st.number_input('enter hight',min_value=1,max_value=100)
  width=st.number_input('enter width',min_value=1,max_value=100)
  area=hight*width

btn=st.button('cal')
if btn:
  with st.spinner('loadind')
  time.sleep(2)
  st.write(f'area:{area}')

