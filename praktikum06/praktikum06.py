import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Identitas Kelompok
st.title("Praktikum 6 - Stacked Bar Chart")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254    
- Alim Rifai - 0110122068
""")

# data gender
stores = ['Store A', 'Store B', 'Store C',]
male = [150, 200, 180]
female = [150, 300, 200]

#data transaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

#data_quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]


#1 Grafik Stacked vertikal Bar Chart
st.subheader("1. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, bottom=male, label='Female', color='pink')

ax.set_title('Population by Gender in Stores')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()
st.pyplot(fig)

#2 Grafik Stacked vertikal Bar Chart
st.subheader("2. Stacked Vertical Bar Chart dengan matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='Green')

ax.set_title('Population by Gender by Stores')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()
st.pyplot(fig)

#3 Grafik Kustomisasi Stacked vertikal Bar Chart
st.subheader("3. Kustomisasi Stacked Vertical Bar Chart")

for i in range(len(x)):
    plt.text(x[i],product_a[i]/2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i],product_a[i]+product_b[i]/2, str(product_b[i]), ha='center', color='black')
st.pyplot(fig)

#4 grafik Multiple Stacked Vertical Bar Chart
st.subheader("4. Multiple Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# quarter 1
ax.bar(x-width/2, q1_male, width, label='Q1 Male', color='lightblue')
ax.bar(x-width/2, q1_female, width, label='Q1 Female', color='pink', bottom=q1_male)

# quarter 2
ax.bar(x+width/2, q2_male, width, label='Q2 Male', color='blue')
ax.bar(x+width/2, q2_female, width, label='Q2 Female', color='red', bottom=q2_male)

ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()
st.pyplot(fig)