import streamlit as st       # Untuk membuat antarmuka aplikasi web
import pandas as pd          # Untuk mengelola data dalam bentuk tabel (DataFrame)
import numpy as np           # Untuk membuat data numerik acak
import altair as alt         # Untuk membuat chart interaktif

# Menampilkan Judul dan Deskripsi
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 2: Data Elements")

# st.markdown() digunakan untuk menampilkan teks dengan format markdown (bullet list, bold, italic, dll.)
st.markdown("""
Kelompok 2:
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# DataFrame : Struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")
df = pd.DataFrame(np.random.randn(30, 10),
                  columns=('col_no %d' % i for i in range(10)))
st.dataframe(df)  # Menampilkan DataFrame dengan fitur interaktif (scrolling, sorting)

# Highlight nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

# Highlight nilai minimum di setiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)
# Untuk menampilkan tabel statis
st.table(df)

# Metrics : Komponen tampilan angka penting
st.subheader("Metrics")
# Menampilkan metrics tunggal (nilai utama + perubahan nilai)

# Metrics Tunggal
st.metric(label="Temperature", value="31 °C", delta="1.2 °C") # kenaikan 1.2 °C

# Metrics sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubahan:
# - "normal" (default): naik -> hijau, turun -> merah
# - "inverse": kebalikannya (naik -> merah, turun -> hijau)
# - "off": tidak menampilkan warna perubahan

# definisikan variabel metrics
col1, col2, col3 = st.columns(3)

# Menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") #netral (tidak baik, tidak buruk)

# Menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) # kosong # naik baik
st.metric(label="Trees", value="91456", delta="-1132649") # turun baik

# Fungsi write() sebagai Superfungsi 
st.subheader("Write Function sebagai Superfungsi")
# Menentukan DataFrame
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
# Menentukan argumen ganda dalam fungsi write
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function") # Menampilkan teks dan DataFrame sekaligus

# Menentukan nilai acak untuk chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b'])
# Menentukan chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])
# Menentukan chart dalam fungsi write
st.write(chart)

# Perhitungan matematika tanpa fungsi yang didefinisikan 
st.subheader("Magic Function")
"Adding 5 & 4 =", 5 + 4
# Menampilkan variabel 'a' beserta nilainya
a = 5
'a', a

# Magic dengan teks markdown
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""
# Menampilkan DataFrame dengan magic
df = pd.DataFrame({'col': [1, 2]})
'dataframe', df