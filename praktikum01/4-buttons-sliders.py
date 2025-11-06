# Import library yang dibutuhkan
import streamlit as st
import time

# Menampilkan Judul dan Deskripsi
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 4: Buttons and Sliders")

# st.markdown() digunakan untuk menampilkan teks dengan format markdown (bullet list, bold, italic, dll.)
st.markdown("""
Kelompok 2:
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Buttons
st.title('Creating a Button')
# Membuat tombol
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

# Radio Buttons
st.title('Creating Radio Buttons')
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male')
elif gender == 'Female':
    st.write("You have selected Female")
else:
    st.write("You have selected Others")

# Checkboxes
st.title('Creating Checkboxes')
st.write('Select your Hobbies:')
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sport')

# Dropdown
st.title('Creating Dropdown')
hobby = st.selectbox('Choose your hobby:',
    ('Books', 'Movies', 'Sports'))

# Multiselect
st.title('Multi-Select')
hobbies = st.multiselect(
    'What are your hobbies?',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)

# Download Button
st.title("Download Button")
down_btn = st.download_button(
    label="Download Image",
    data=open("assets/cat.jpg", "rb"),
    file_name="cat.jpg",
    mime="image/jpg"
)

# Progress Bar
st.title('Progress Bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)
st.write('Download Completed')

# Spinner
st.title('Spinner')
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')