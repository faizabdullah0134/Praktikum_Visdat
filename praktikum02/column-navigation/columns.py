import streamlit as st

st.title("Praktikum 2 - Columns")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in Column 1
col1.write("First Column")
col1.image("assets/cat.jpg")
# Inserting Elements in Column 2
col2.write("Second Column")
col2.image("assets/tiger.jpg")