import streamlit as st
import numpy as np
import time

st.title("Praktikum 2 - Containers")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

st.title("Containers")
with st.container():
    st.write("Elements inside the container")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside the container")

st.title("Out of Order Container")
# Defining Containers
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")
# Now insert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))

# Empety Container
with st.container():
    for second in range(5):
        st.write(f"⏳ {second} seconds have passed")
        time.sleep(1)
        st.write("✓ Times up!!!")