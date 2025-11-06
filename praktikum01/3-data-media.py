import streamlit as st
import base64
from PIL import Image

# Menampilkan Judul dan Deskripsi
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 3: Data and Media Elements")

# st.markdown() digunakan untuk menampilkan teks dengan format markdown (bullet list, bold, italic, dll.)
st.markdown("""
Kelompok 2:
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Images
st.write("Displaying an Images")
st.image("assets/cat.jpg")
st.write("Image Courtesy: instagram meme")

st.write("Displaying Multiple Images")
animal_images = [
    'assets/lion.jpg',
    'assets/cheetah.jpg',
    'assets/cat.jpg',
    'assets/tiger.jpeg',
]
st.image(animal_images, width=150)
st.write("Image Courtesy: Many Sources")

# Background Image
def add_local_background_image_(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
add_local_background_image_('assets/sky.jpg')

# Resizing Image
original_image = Image.open("assets/cat.jpg")
st.title("Original Image")
st.image(original_image)

resized_image = original_image.resize((600, 400))
st.title("Resized Image")
st.image(resized_image)
