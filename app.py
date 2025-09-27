import streamlit as st
import time

# ---------- Custom CSS for hacker desktop splash ----------
st.markdown("""
    <style>
    body, .stApp {
        background: #000 !important;
    }
    .glow {
        font-family: 'Orbitron', monospace, sans-serif;
        font-size: 60px;
        color: #fff;
        text-align: center;
        letter-spacing: 10px;
        text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #0ff, 0 0 40px #0ff;
        margin-top: 100px;
        animation: flicker 1.5s infinite alternate;
    }
    @keyframes flicker {
      0% { opacity: 1; text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #0ff, 0 0 40px #0ff;}
      50% { opacity: 0.7; text-shadow: 0 0 20px #fff, 0 0 30px #0ff, 0 0 40px #0ff, 0 0 60px #0ff;}
      100% { opacity: 1; text-shadow: 0 0 12px #fff, 0 0 24px #0ff, 0 0 36px #0ff, 0 0 48px #0ff;}
    }
    .loading-msg {
        color: #aaa;
        text-align: center;
        font-size: 22px;
        margin-bottom: 10px;
        font-family: 'Roboto Mono', monospace;
    }
    .init-status {
        color: #fff;
        text-align: center;
        margin-top: 10px;
        font-size: 18px;
        font-family: 'Roboto Mono', monospace;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Roboto+Mono&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ---------- Splash Animation ----------
loading_msgs = [
    "In",
    "Loading essential services..",
    "Configuring security protocols...",
    "Launching interface..."
]

progress_bar = st.empty()
glow_header = st.markdown('<div class="glow">ZAP</div>', unsafe_allow_html=True)
loadmsg = st.empty()
statusmsg = st.empty()

for i in range(101):
    if i < 25:
        msg = loading_msgs[0]
    elif i < 50:
        msg = loading_msgs[1]
    elif i < 85:
        msg = loading_msgs[2]
    else:
        msg = loading_msgs[3]
    loadmsg.markdown(f'<div class="loading-msg">{msg}</div>', unsafe_allow_html=True)
    progress_bar.progress(i)
    statusmsg.markdown(f'<div class="init-status">System initialization: {i}%</div>', unsafe_allow_html=True)
    time.sleep(0.035)

# ---------- Clear splash elements ----------
glow_header.empty()
loadmsg.empty()
progress_bar.empty()
statusmsg.empty()

# ---------- Portfolio Headings Table of Contents ----------
st.markdown("""
    <div style="background: #111; border-radius: 8px; padding: 18px; color: #0ff; margin-bottom: 16px; text-align:center;">
        <h3 style="font-family: 'Orbitron', monospace; color: #fff;">PORTFOLIO</h3>
        <ul style="list-style:none; padding:0; font-family:'Roboto Mono', monospace;">
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

st.write("Feel free to connect with me on LinkedIn or check out my GitHub and TryHackMe profiles!")
