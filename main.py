import streamlit as st

st.title('아잉!')
name = st.text_input('이름을 입력하세요 : ')
menu = st.selectbox('가장 많이 쓰는 앱은?' :', ['유튜브', '인스타', '카톡'])
time = st.slider('하루 사용 시간은?', 0, 12, 3)
if st.button('나의 
