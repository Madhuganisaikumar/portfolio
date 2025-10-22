import streamlit as st
import os

# --------------------------
# Page setup
# --------------------------
st.set_page_config(page_title="Madhugani Sai Kumar | Portfolio", page_icon="💻", layout="wide")

# --------------------------
# Load static files
# --------------------------
def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

html_content = load_file("index.html")
css_content = load_file("styles.css")
js_content = load_file("script.js")

# --------------------------
# Replace default details with your info
# --------------------------
html_content = html_content.replace("Abhijeet Bhale", "Madhugani Sai Kumar")
html_content = html_content.replace("abhijeetbhale7@gmail.com", "your.email@example.com")
html_content = html_content.replace(
    "An aspiring Full Stack Developer passionate about building sleek web experiences.",
    "Python Developer | AI + Blockchain | Building intelligent systems with modern UI experiences."
)
html_content = html_content.replace(
    "I'm currently pursuing my B.Tech in Computer Science Engineering at Medicaps University, Indore.",
    "Currently pursuing B.Tech in Computer Science and Engineering, focusing on AI and Full Stack development."
)
html_content = html_content.replace(
    "Abhijeet Bhale Resume Updated 300925.pdf",
    "resume.pdf"
)

# --------------------------
# Inject CSS and JS into HTML
# --------------------------
full_page = f"""
<html>
    <head>
        <style>
        {css_content}
        </style>
    </head>
    <body>
        {html_content}
        <script>
        {js_content}
        </script>
    </body>
</html>
"""

# --------------------------
# Display in Streamlit
# --------------------------
st.components.v1.html(full_page, height=1200, scrolling=True)
