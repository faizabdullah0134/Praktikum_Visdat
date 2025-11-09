import streamlit as st
from PIL import Image

st.title("Praktikum 2 - Columns with Padding")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

img = Image.open("assets/cat.jpg")
st.title("Padding")
# Defining Padding with Columns
col1, padding, col2 = st.columns([10, 2, 10])
with col1:
    col1.image(img)
with col2:
    col2.image(img)