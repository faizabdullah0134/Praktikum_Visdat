import streamlit as st
import matplotlib.pyplot as plt

# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# Layout streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot",
                                                         "Multiple & Customizations",
                                                         "Jenis Garis untuk Menunjukkan Tren",
                                                         "Subplot"))

# Identitas Kelompok
st.title("Praktikum 3 - Line Plot")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.set_title('Penjualan Product A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Multiple Lines with Customizations
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='orange', linestyle='-', marker='x')
    ax.set_title('Penjualan Product per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Data Sample Tambahan
product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]

# Line Types to Show Trends
def tren_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='orange', linestyle='-', marker='x')
    ax.plot(months, product_C_sales, label='Product C', color='green', linestyle=':', marker='o')
    ax.plot(months, product_D_sales, label='Product D', color='red', linestyle='-.', marker='x')
    ax.set_title('Tren Penjualan Product per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Subplots
def subplots():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    # Plot untuk Product A
    ax1.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax1.set_title('Penjualan Product A per Bulan')
    ax1.set_xlabel('Bulan')
    ax1.set_ylabel('Penjualan')
    ax1.legend()
    ax1.grid(True)

    # Plot untuk Product B
    ax2.plot(months, product_B_sales, label='Product B', color='orange', linestyle='-', marker='x')
    ax2.set_title('Penjualan Product B per Bulan')
    ax2.set_xlabel('Bulan')
    ax2.set_ylabel('Penjualan')
    ax2.legend()
    ax2.grid(True)

    fig.tight_layout()
    st.pyplot(fig)

# Logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customizations":
    customize_line_plot()
elif option == "Jenis Garis untuk Menunjukkan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()
