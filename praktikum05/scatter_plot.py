import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Dataset utama
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Dataset tambahan (Penjualan)
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekends = [60, 70, 80, 100, 110, 120, 140, 160, 180]

# data untuk analisis
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Coklat': [40, 45, 50, 55, 60, 65, 70, 75, 80],
    'Penjualan_Vanila': [82, 80, 78, 76, 77, 80, 82, 85, 88],
    'Penjualan_Stroberi': [55, 50, 55, 60, 65, 60, 65, 70, 72],
    'Kelembapan': [50, 65, 70, 75, 80, 85, 90, 95, 100]
}

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Layout Utama
options = st.sidebar.selectbox("Pilih contoh scatter plot:",
                               ("Basic Scatter Plot",
                                "Kustomisasi Scatter Plot",
                                "Multiple Scatter Plot",
                                "Analisis Scatter Plot"))

# Identitas Kelompok
st.title("Praktikum 5 - Scatter Plot")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254    
- Alim Rifai - 0110122068
""")

# 1. Basic Scatter Plot
def basic_scatter_plot():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2. Kustomisasi Scatter Plot
def custom_scatter_plot():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 3. Multiple Scatter Plot
def multiple_scatter_plot():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_weekends, color='purple', label='Akhir Pekan', s=80)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 4. Analisis Scatter Plot
def scatter_3_variable():
    st.subheader("4. Analisis Scatter Plot")
    # Opsi jenis es krim
    jenis_eskrim = st.selectbox("Pilih Jenis Es Krim:", ["Coklat", "Vanila", "Stroberi"])

    # Logika untuk opsi jenis eskirm berdasarkan pilihan
    if jenis_eskrim == "Coklat":
        penjualan = df['Penjualan_Coklat']
    elif jenis_eskrim == "Vanila":
        penjualan = df['Penjualan_Vanila']          
    elif jenis_eskrim == "Stroberi":
        penjualan = df['Penjualan_Stroberi']

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    # Scatter Plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7, edgecolor='black')

    # Styling
    ax.set_title(f"Hubungan Penjualan {jenis_eskrim} vs Suhu dan Kelembapan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel(f"Penjualan Es Krim {jenis_eskrim}")
    fig.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)

    # ringkasan hubungan
    st.subheader("Analisis Hubungan")
    st.write(f'Grafik menunjukkan hubungan antara suhum kelembapan, dan penjualan es krim **{jenis_eskrim}**.')

# Routing berdasarkan menu sidebar
if options == "Basic Scatter Plot":
    basic_scatter_plot()
elif options == "Kustomisasi Scatter Plot":
    custom_scatter_plot()
elif options == "Multiple Scatter Plot":
    multiple_scatter_plot()
elif options == "Analisis Scatter Plot":
    scatter_3_variable()