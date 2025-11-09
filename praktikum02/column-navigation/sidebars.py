import streamlit as st

st.title("Praktikum 2 - Sidebars")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User?", ("Yes", "No"))
st.sidebar.slider("Select a Number", 0, 10)