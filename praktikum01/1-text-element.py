# Import Library yang Dibutuhkan
import streamlit as st

# Text Element
# Header - untuk menampilkan teks header
st.header("Ini Header")
st.subheader("Ini Subheader")
st.text("Ini Text Biasa")
st.markdown("**Ini text bold** *dan ini italic*")
st.caption("Ini Caption")
st.title("Ini Judul")

# Coba Mandiri
st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1: Text Element")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Bagian 2: Menampilkan Rumus (LaTeX)
st.header("Displaying LaTeX")
st.latex(r''' \cos^2\theta = 1 - 2\sin^2\theta ''') # Rumus Trigonometri
st.latex(r''' (a + b)^2 = a^2 + b^2 + 2ab ''') # Rumus kuadrat binomial

# Bagian 3: Menampilkan Code
st.header("Displaying Code")
st.header("Displaying Python Code")
st.subheader("Python Code")
code = '''
def hello():
    print("Hello, Streamlit!")
'''

# st.code() digunakan untuk menampilkan kode dengan format yang rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
public class GFG {
    public static void main(String args[]) {
        System.out.println("Hello World");
    }
}
""", language='java')
# Fungsi st.code() bisa digunakan untuk bahasa pemrograman lain seperti Java, JavaScript, C++, HTML, dll.

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    adddlert("Welcome guest!");
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script>
""", language='javascript')
# Kode ini menunjukkan contoh bagaimana menangani error (exeption) di Javascript.
# Hasilnya tidak dijalankan di Streamlit, hanya ditampilkan sebagai contoh kode.