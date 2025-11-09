import streamlit as st
from PIL import Image

st.title("Praktikum 2 - Spaced Out Columns")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

img = Image.open("assets/cat.jpg")
st.title("Spaced Out Columns")
# Defining two Rows
for i in range(2):
# Defining no. of columns with size
    cols = st.columns([3, 1, 2, 1])
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)