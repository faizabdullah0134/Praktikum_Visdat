import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#judul
st.title("Praktikum 7 visualisasi data")
st.subheader("Horizontal Bar Chart & Stacked Horizontal Bar Chart")

# Identitas Kelompok
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254    
- Alim Rifai - 0110122068
""")

#dataset
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 200]
sales_2024 = [300, 450, 320, 300]

# filter kategori
kategori = st.selectbox(
    "Pilih Kategori Visualisasi",
    ['Basic Chart', 'Kustomisasi Grafik', 'Multiple Chart']
)

# basic chart
if kategori == 'Basic Chart':
    st.subheader("Horizontal Bar Chart")
    fig1, ax1 = plt.subplots()

    #grafik batang horizontal
    ax1.set_title("Horizontal Bar Chart (2023)")
    ax1.set_xlabel("Jumlah Penjualan")
    ax1.set_ylabel("Merek")
    ax1.barh(brands, sales_2023, color='skyblue')
    st.pyplot(fig1)

    #Stacked
    st.subheader("Stacked Horizontal Bar Chart Sederhana")
    fig2, ax2 = plt.subplots()
    ax2.set_title("Stacked Horizontal Bar Chart (2023)")
    ax2.set_xlabel("Jumlah Penjualan")
    ax2.set_ylabel("Merek")
    ax2.barh(brands, sales_2023, color='skyblue', label='2023')
    ax2.barh(brands, sales_2024, left=sales_2023, color='lightgreen', label='2024')
    ax2.legend()
    st.pyplot(fig2)

# kustomisasi grafik
elif kategori == 'Kustomisasi Grafik':
    st.subheader("Kustomisasi Horizontal Bar Chart")
    fig3, ax3 = plt.subplots()

    ax3.set_title("Kustomisasi Horizontal Bar Chart (2023)")
    ax3.set_xlabel("Jumlah Penjualan")
    ax3.set_ylabel("Merek")
    ax3.barh(brands, sales_2023, color='lightblue', edgecolor='black')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)
    st.pyplot(fig3)

    #label nilai
    for i, v in enumerate(sales_2023):
        ax3.text(v + 5, i, str(v), color='black', va='center')
