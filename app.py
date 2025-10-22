import streamlit as st

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Madhugani Sai Kumar | Portfolio",
    page_icon="💻",
    layout="wide"
)

# ---------------------------
# PORTFOLIO DATA
# ---------------------------
profile = {
    "name": "Madhugani Sai Kumar",
    "title": "Full Stack Developer | Machine Learning | Blockchain Enthusiast",
    "about": """Hi 👋 I'm Madhugani, a passionate Python developer who builds intelligent and scalable apps. 
Currently working on **ChainGuardian** (AI + Blockchain anti-fraud system) and **Medical Report Analyzer** using LLMs and OCR.""",
    "skills": [
        "Python", "Flask", "Streamlit", "React", "Node.js",
        "MongoDB", "MySQL", "Machine Learning", "Blockchain", "Git", "AWS"
    ],
    "projects": [
        {
            "name": "ChainGuardian",
            "desc": "AI-powered blockchain reputation system to detect and prevent fraud in e-commerce.",
            "tech": ["Python", "Solidity", "Streamlit", "IPFS"]
        },
        {
            "name": "Medical Report Analyzer",
            "desc": "LLM-based system for extracting structured insights from unstructured medical PDFs.",
            "tech": ["Python", "LangChain", "OpenAI API", "Streamlit"]
        },
        {
            "name": "Smart Portfolio",
            "desc": "This live Streamlit portfolio app built entirely in Python!",
            "tech": ["Streamlit"]
        }
    ],
    "journey": [
        ("B.Tech Computer Science", "Medicaps University, Indore (2022–2026)"),
        ("Hackathon Project", "ChainGuardian - AI & Blockchain anti-fraud system"),
        ("AI Project", "Medical Report Analyzer - LLM + OCR pipeline")
    ],
    "contact": {
        "email": "your.email@example.com",
        "linkedin": "https://linkedin.com/in/yourprofile",
        "github": "https://github.com/yourusername",
        "instagram": "https://instagram.com/yourprofile"
    }
}

# ---------------------------
# PAGE STYLE
# ---------------------------
st.markdown("""
<style>
body, .stApp {
    background: radial-gradient(circle at top left, #020202, #0c0c0c);
    color: #e0e0e0;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3 {
    color: #1DCD9F;
}
.stButton > button {
    background: linear-gradient(90deg, #1DCD9F, #1B9DB8);
    color: white;
    font-weight: 600;
    border-radius: 8px;
    border: none;
}
.stButton > button:hover {
    background: linear-gradient(90deg, #19b08b, #17829e);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER SECTION
# ---------------------------
st.title(profile["name"])
st.subheader(profile["title"])
st.markdown(profile["about"])

# ---------------------------
# SKILLS SECTION
# ---------------------------
st.markdown("## 🧠 Skills")
cols = st.columns(3)
for i, skill in enumerate(profile["skills"]):
    cols[i % 3].markdown(f"- {skill}")

# ---------------------------
# PROJECTS SECTION
# ---------------------------
st.markdown("## 🚀 Projects")
for p in profile["projects"]:
    with st.container():
        st.markdown(f"### {p['name']}")
        st.markdown(p["desc"])
        st.markdown(f"**Tech Stack:** {', '.join(p['tech'])}")
        st.divider()

# ---------------------------
# JOURNEY SECTION
# ---------------------------
st.markdown("## 🧭 Journey")
for title, desc in profile["journey"]:
    st.markdown(f"**{title}** — {desc}")

# ---------------------------
# CONTACT SECTION
# ---------------------------
st.markdown("## 📬 Contact")
st.markdown(f"📧 Email: [{profile['contact']['email']}]({profile['contact']['email']})")
st.markdown(f"💼 [LinkedIn]({profile['contact']['linkedin']})")
st.markdown(f"🐙 [GitHub]({profile['contact']['github']})")
st.markdown(f"📸 [Instagram]({profile['contact']['instagram']})")

# ---------------------------
# FOOTER
# ---------------------------
st.divider()
st.caption("© 2025 Madhugani Sai Kumar | Built entirely in Python & Streamlit 💚")
