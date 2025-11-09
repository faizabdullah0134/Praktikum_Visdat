import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Bar Chart")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=['C1', 'C2', 'C3', 'C4']
)

st.bar_chart(df)