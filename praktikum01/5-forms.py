# Import library yang dibutuhkan
import streamlit as st
import datetime
import pandas as pd

# Menampilkan Judul dan Deskripsi
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 5: Forms")

# st.markdown() digunakan untuk menampilkan teks dengan format markdown (bullet list, bold, italic, dll.)
st.markdown("""
Kelompok 2:
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Text Box
st.title("Text Box")
# Membuat text box
name = st.text_input("Enter your name")
st.write("Your name is", name)

# Text Area
# Membuat text area
input_text = st.text_area("Enter your review")
st.write("""You entered: \n""", input_text)

# Number Input
# Membuat number input
st.number_input("Enter your number")
num = st.number_input("Enter your number", 0, 10, 5, 2)
st.write("Min. value is 0, \nMax. value is 10")
st.write("Default value is 5, \nStep size value is 2")
st.write("Total value after adding number entered with step values is:", num)

# Time Input
st.title("Time")
# Membuat time function
st.time_input("Select your time")

# Date Input
st.title("Date")
# Membuat date function
st.date_input("Select date")

# Date Input with initial, min, and max value
st.date_input(
    "Select your date",
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1)
)

# Color Picker
st.title("Select color")
# Membuat color picker
color_code = st.color_picker("Select your color")
st.header(color_code)

# Dataset Upload (CSV)
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check details")
if details:
    if data_file is not None:
        file_details = {"file_name": data_file.name, "file_type": data_file.type, "file_size": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

# Submit Button
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Membuat submit button
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)