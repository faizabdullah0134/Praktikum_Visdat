import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Map")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

df = pd.DataFrame(
    np.random.randn(50, 2) / [10, 10] + [15.4589, 75.0078],
    columns=['latitude', 'longitude']
)

st.map(df)