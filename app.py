import streamlit as st
import time

# ---------- Custom CSS for background and headings ----------
st.markdown("""
    <style>
    .welcome-container {
        background: url('https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=1500&q=80') no-repeat center center;
        background-size: cover;
        padding: 40px 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
    }
    .toc {
        background: #222;
        border-radius: 6px;
        padding: 12px;
        color: #fff;
        font-size: 1.1em;
        margin-bottom: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Welcome Section on Black Background ----------
st.markdown("""
    <div class="welcome-container">
        <h1>Welcome</h1>
    </div>
""", unsafe_allow_html=True)

# ---------- Loading Bar ----------
st.write("Loading your portfolio...")
progress = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress.progress(percent_complete + 1)

# ---------- Table of Contents (Headings Preview) ----------
st.markdown("""
    <div class="toc">
        <h3>Portfolio Sections</h3>
        <ul>
            <li>Projects</li>
            <li>Certifications</li>
            <li>Resume</li>
            <li>GitHub</li>
            <li>TryHackMe</li>
            <li>LinkedIn</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# ---------- Sidebar with your links ----------
st.sidebar.title("Navigation")
st.sidebar.markdown("[Resume](https://drive.google.com/file/d/1cM77ga8TZzhngI30XniL03WammTL4PHU/view?usp=sharing)")
st.sidebar.markdown("[GitHub](https://github.com/Madhuganisaikumar)")
st.sidebar.markdown("[THM](https://tryhackme.com/p/Madhuganisai)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/sai-madhugani/)")

# ---------- Main Portfolio Sections ----------
with st.expander("Projects"):
    st.image("https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/project1.png", caption="Zero Trust Blockchain")
    st.image("https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/project2.png", caption="KLCybersac")
    st.image("https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/project3.png", caption="Career Portal")

with st.expander("Certifications"):
    st.image("https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/cert1.png", caption="Certified Ethical Hacker")
    st.image("https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/cert2.png", caption="AI Associate")
    st.image("https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/cert3.png", caption="Google Cloud Cybersecurity")
    st.image("https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/cert4.png", caption="Red Hat Developer")
