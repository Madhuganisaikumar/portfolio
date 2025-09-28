import streamlit as st
import time
import datetime

# Replace this with your shareable image link (direct image link ideally)
BG_IMAGE_URL = "https://drive.google.com/uc?export=view&id=1jIiXUwNK6WxIT6FlDkHNIiw80TdK1J74"

# ---------- CSS + background image insertion ----------
st.markdown(f"""
    <style>
    body, .stApp {{
        background: #000;  /* fallback black */
        position: relative;
        overflow: hidden;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: url("{BG_IMAGE_URL}") no-repeat center center;
        background-size: cover;  /* or adjust as needed: contain, 50%, etc */
        opacity: 0.05;  /* change this to make it more or less visible */
        z-index: -1;
    }}
    .glow {{
        font-family: 'Orbitron', monospace, sans-serif;
        font-size: 60px;
        color: #fff;
        text-align: center;
        letter-spacing: 10px;
        text-shadow: 0 0 10px #fff, 0 0 20px #0ff, 0 0 30px #0ff, 0 0 40px #0ff;
        margin-top: 100px;
        animation: flicker 1.5s infinite alternate;
    }}
    @keyframes flicker {{
      0% {{ opacity: 1; text-shadow: 0 0 10px #fff, 0 0 20px #0ff, 0 0 30px #0ff, 0 0 40px #0ff; }}
      50% {{ opacity: 0.7; text-shadow: 0 0 20px #fff, 0 0 30px #0ff, 0 0 40px #0ff, 0 0 60px #0ff; }}
      100% {{ opacity: 1; text-shadow: 0 0 14px #fff, 0 0 24px #0ff, 0 0 36px #0ff, 0 0 48px #0ff; }}
    }}
    .loading-msg {{
        color: #aaa;
        text-align: center;
        font-size: 22px;
        margin-bottom: 10px;
        font-family: 'Roboto Mono', monospace;
    }}
    .init-status {{
        color: #fff;
        text-align: center;
        margin-top: 10px;
        font-size: 18px;
        font-family: 'Roboto Mono', monospace;
    }}
    .sidebar-icons img {{ width: 40px; margin-bottom: 10px; }}
    .sidebar-icons .icon-label {{
        margin-bottom: 30px;
        font-size: 18px;
        font-family: 'Segoe UI', Arial, sans-serif;
        color: #fff;
    }}
    .center-logo {{
        display: flex;
        align-items: center;
        justify-content: center;
        height: 60vh;
    }}
    .center-logo img {{ max-width: 380px; }}
    .taskbar {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100vw;
        background: #222d35;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 60px;
        z-index: 100;
    }}
    .taskbar-icons {{
        display: flex;
        align-items: center;
        gap: 30px;
    }}
    .taskbar-icons .icon-box {{
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #fff;
        font-size: 14px;
        margin: 0 12px;
    }}
    .taskbar-icons img {{ width: 36px; margin-bottom: 4px; }}
    .taskbar-datetime {{
        position: absolute;
        right: 36px;
        color: #fff;
        background: rgba(40,40,40,0.9);
        padding: 8px 18px;
        border-radius: 8px;
        font-size: 16px;
    }}
    @media (max-width: 768px) {{
        .glow {{ font-size: 36px; letter-spacing: 4px; margin-top: 60px; }}
        .taskbar {{ flex-direction: column; height: auto; padding: 10px; }}
        .taskbar-icons {{ gap: 15px; }}
    }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Roboto+Mono&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


def splash_screen():
    loading_msgs = [
        "In",
        "Loading essential services..",
        "Configuring security protocols...",
        "Launching interface..."
    ]
    progress_bar = st.empty()
    glow_header = st.empty()
    loadmsg = st.empty()
    statusmsg = st.empty()
    glow_header.markdown('<div class="glow">ZAP</div>', unsafe_allow_html=True)
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
        time.sleep(0.02)
    glow_header.empty()
    loadmsg.empty()
    progress_bar.empty()
    statusmsg.empty()
    st.session_state.loaded = True


if "loaded" not in st.session_state:
    splash_screen()

# Sidebar icons
st.sidebar.markdown("""
    <div class="sidebar-icons">
        <a href="https://drive.google.com/file/d/1cM77ga8TZzhngI30XniL03WammTL4PHU/view?usp=sharing" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/resume.png"/>
            <div class="icon-label">Resume</div>
        </a>
        <a href="https://github.com/Madhuganisaikumar" target="_blank">
            <img src="https://img.icons8.com/material-rounded/48/000000/github.png"/>
            <div class="icon-label">GitHub</div>
        </a>
        <a href="https://tryhackme.com/p/Madhuganisai" target="_blank">
            <img src="https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/thm_icon.png"/>
            <div class="icon-label">THM</div>
        </a>
        <a href="https://www.linkedin.com/in/sai-madhugani/" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/linkedin-circled.png"/>
            <div class="icon-label">Linkedin</div>
        </a>
    </div>
""", unsafe_allow_html=True)

# Center ZAP Logo (if you still want a central logo too)
st.markdown("""
    <div class="center-logo">
        <img src="https://raw.githubusercontent.com/Madhuganisaikumar/portfolio/main/zap_logo.png" alt="ZAP Logo"/>
    </div>
""", unsafe_allow_html=True)

# Taskbar with live date/time
time_placeholder = st.empty()

# Wrap in a container so other content can come above
with time_placeholder:
    now = datetime.datetime.now()
    time_html = f"""
        <div class="taskbar">
            <div class="taskbar-icons">
                <div class="icon-box">
                    <img src="https://img.icons8.com/external-outline-juicy-fish/60/external-terminal-coding-outline-outline-juicy-fish.png"/>
                    Terminal
                </div>
                <div class="icon-box">
                    <img src="https://img.icons8.com/external-flatart-icons-outline-flatarticons/64/external-folder-basic-ui-elements-flatart-icons-outline-flatarticons-1.png"/>
                    Certifications
                </div>
                <div class="icon-box">
                    <img src="https://img.icons8.com/ios-filled/50/stack-of-photos.png"/>
                    Projects
                </div>
            </div>
            <div class="taskbar-datetime">
                {now.strftime("%a, %b %d, %Y")} | {now.strftime("%I:%M:%S %p")}
            </div>
        </div>
    """
    st.markdown(time_html, unsafe_allow_html=True)
