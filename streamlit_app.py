import streamlit as st
area=None
st.header('calculate area')
choose=st.selectbox('choose box',['circle','trangle'])
if choose=='circle' :
  r=st.number_input('enter radius',min_value=1,max_value=100)
  area=3.14*r*r
elif choose=='trangle' :
  hight=st.number_input('enter hight',min_value=1,max_value=100)
  width=st.number_input('enter width',min_value=1,max_value=100)
  area=3.14*hight*width

btn=st.button('cal')
if btn:
  st.write(f'area{area}')

