import streamlit as st

st.set_page_config(
    page_title="Madhugani Sai Kumar | Desktop Portfolio",
    page_icon="💻",
    layout="wide"
)

# --- CSS + HTML in one go --- #
html = r"""
<style>
/* Hide default Streamlit chrome for cleaner desktop look */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Global */
body, .stApp {
  background: radial-gradient(circle at top, #030712 0%, #020617 45%, #000 100%);
  color: #e5e7eb;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Boot / loading screen */
.boot-screen {
  position: fixed;
  inset: 0;
  background: #020617;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #22c55e;
  font-family: "Courier New", monospace;
  z-index: 10;
  animation: bootFade 4s forwards;
}

.boot-title {
  font-size: 20px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.boot-line {
  font-size: 14px;
  margin: 3px 0;
  opacity: 0;
  animation: typeLine 0.6s forwards;
}

.boot-line:nth-child(2) { animation-delay: 0.3s; }
.boot-line:nth-child(3) { animation-delay: 0.7s; }
.boot-line:nth-child(4) { animation-delay: 1.1s; }
.boot-line:nth-child(5) { animation-delay: 1.6s; }
.boot-line:nth-child(6) { animation-delay: 2.0s; }

.boot-cursor {
  display: inline-block;
  width: 8px;
  background: #22c55e;
  margin-left: 4px;
  animation: blink 0.9s infinite;
  height: 14px;
  vertical-align: middle;
}

@keyframes typeLine {
  from {opacity: 0; transform: translateY(6px);}
  to   {opacity: 1; transform: translateY(0);}
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%,100%{ opacity: 0; }
}

@keyframes bootFade {
  0%   { opacity: 1; }
  75%  { opacity: 1; }
  100% { opacity: 0; pointer-events: none; }
}

/* Desktop root */
.desktop-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  opacity: 0;
  animation: desktopIn 4s forwards;
}

@keyframes desktopIn {
  0%,60% { opacity: 0; }
  100%   { opacity: 1; }
}

/* Desktop background */
.desktop {
  flex: 1;
  background:
    radial-gradient(circle at top left, rgba(34,197,94,0.12), transparent 55%),
    radial-gradient(circle at bottom right, rgba(56,189,248,0.1), transparent 50%),
    #020617;
  padding: 18px 22px 10px;
  display: flex;
}

/* "Icons" area and "windows" area */
.desktop-left {
  width: 210px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.desktop-right {
  flex: 1;
  margin-left: 16px;
  position: relative;
}

/* Icons */
.icon {
  width: 88px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  text-align: center;
  font-size: 11px;
  color: #e5e7eb;
  text-shadow: 0 1px 2px rgba(0,0,0,0.7);
}

.icon-row {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.icon-badge {
  width: 54px;
  height: 54px;
  border-radius: 14px;
  background: radial-gradient(circle at top, #0f172a, #020617);
  border: 1px solid rgba(148,163,184,0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 22px rgba(15,23,42,0.9);
  position: relative;
}

.icon-badge::before {
  content: "";
  position: absolute;
  inset: -30%;
  background: radial-gradient(circle at top, rgba(34,197,94,0.4), transparent 65%);
  opacity: 0;
  transition: opacity 0.25s ease;
}

.icon:hover .icon-badge::before {
  opacity: 1;
}

/* Simple emoji "logos" */
.icon-emoji {
  font-size: 26px;
}

/* Taskbar */
.taskbar {
  height: 32px;
  background: linear-gradient(to right, #020617, #020617, #020617);
  border-top: 1px solid rgba(15,23,42,1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 12px;
  font-size: 11px;
  color: #9ca3af;
}
.taskbar-left {
  display: flex;
  align-items: center;
  gap: 6px;
}
.taskbar-logo {
  width: 18px;
  height: 18px;
  border-radius: 999px;
  background: radial-gradient(circle at top, #22c55e, #16a34a);
  box-shadow: 0 0 12px rgba(34,197,94,0.8);
}
.taskbar-center {
  display: flex;
  gap: 10px;
}
.taskbar-pill {
  padding: 3px 8px;
  border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.6);
  background: rgba(15,23,42,0.9);
  color: #e5e7eb;
}
.taskbar-right span {
  margin-left: 8px;
}

/* Window base */
.window {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  border: 1px solid rgba(148,163,184,0.7);
  background: radial-gradient(circle at top, rgba(15,23,42,0.97), #020617);
  box-shadow: 0 22px 55px rgba(15,23,42,0.98);
  padding: 12px 14px;
  display: none; /* default hidden */
  flex-direction: column;
  font-size: 13px;
}

/* Show window when target matched */
#win-resume:target,
#win-projects:target,
#win-github:target,
#win-linkedin:target {
  display: flex;
}

/* If none target, show resume window by default */
.desktop-right:not(:has(.window:target)) #win-resume {
  display: flex;
}

.window-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}
.window-title {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: #9ca3af;
}
.window-buttons {
  display: flex;
  gap: 4px;
}
.win-dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
}
.win-close { background:#ef4444; }
.win-min   { background:#facc15; }
.win-max   { background:#22c55e; }
.win-body {
  flex: 1;
  padding-top: 4px;
  color: #e5e7eb;
}

/* Resume window content */
.resume-grid {
  display: grid;
  grid-template-columns: minmax(0,1.3fr) minmax(0,1fr);
  gap: 14px;
}
@media (max-width: 900px) {
  .resume-grid {
    grid-template-columns: 1fr;
  }
}
.resume-name {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 3px;
}
.resume-role {
  font-size: 13px;
  color: #a5b4fc;
  margin-bottom: 10px;
}
.resume-about {
  font-size: 13px;
  color: #e5e7eb;
  line-height: 1.6;
}
.resume-section-title {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: #9ca3af;
  margin-top: 8px;
  margin-bottom: 4px;
}
.resume-list {
  font-size: 13px;
  color: #d1d5db;
}
.resume-list li {
  margin-bottom: 3px;
}

/* Projects window */
.project-card {
  border-radius: 14px;
  border: 1px solid rgba(148,163,184,0.6);
  background: radial-gradient(circle at top, rgba(15,23,42,0.96), #020617);
  padding: 10px 11px;
  margin-bottom: 10px;
}
.project-title {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 4px;
}
.project-tag {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: #9ca3af;
  margin-bottom: 3px;
}
.project-desc {
  font-size: 13px;
  color: #d1d5db;
  line-height: 1.5;
}
.project-tech {
  margin-top: 5px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  font-size: 11px;
}
.project-tech span {
  padding: 2px 7px;
  border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.6);
}

/* Link windows */
.link-block {
  border-radius: 14px;
  border: 1px dashed rgba(148,163,184,0.7);
  padding: 10px 11px;
  background: rgba(15,23,42,0.9);
}
.link-label {
  font-size: 12px;
  color: #9ca3af;
  margin-bottom: 4px;
}
.link-main {
  font-size: 13px;
  color: #e5e7eb;
}
.link-main a {
  color: #38bdf8;
}
.link-main a:hover {
  text-decoration: underline;
}

/* Close link style */
.close-link {
  font-size: 11px;
  color: #9ca3af;
  text-decoration: none;
}

/* Small scroll inside window */
.win-body-inner {
  overflow-y: auto;
  max-height: calc(100vh - 140px);
  padding-right: 4px;
}

/* Animations */
@keyframes desktopPulse {
  0% { box-shadow: 0 0 0 0 rgba(34,197,94,0.3); }
  100%{ box-shadow: 0 0 0 12px rgba(34,197,94,0); }
}
</style>

<div class="boot-screen">
  <div class="boot-title">MSK_DESKTOP v1.0</div>
  <div class="boot-line">[ OK ] Initializing Python runtime<span class="boot-cursor"></span></div>
  <div class="boot-line">[ OK ] Loading Streamlit UI modules</div>
  <div class="boot-line">[ OK ] Mounting portfolio filesystem</div>
  <div class="boot-line">[ OK ] Linking projects: ChainGuardian, MedReport Analyzer</div>
  <div class="boot-line">[ OK ] Network: GitHub, LinkedIn online</div>
  <div class="boot-line">[ READY ] Launching MSK_DESKTOP...</div>
</div>

<div class="desktop-wrapper">
  <div class="desktop">
    <div class="desktop-left">
      <div class="icon-row">
        <a href="#win-resume" class="icon">
          <div class="icon-badge">
            <div class="icon-emoji">📄</div>
          </div>
          <span>Resume</span>
        </a>
        <a href="#win-projects" class="icon">
          <div class="icon-badge">
            <div class="icon-emoji">📂</div>
          </div>
          <span>Projects</span>
        </a>
      </div>

      <div class="icon-row">
        <a href="#win-github" class="icon">
          <div class="icon-badge">
            <div class="icon-emoji">🐙</div>
          </div>
          <span>GitHub</span>
        </a>
        <a href="#win-linkedin" class="icon">
          <div class="icon-badge">
            <div class="icon-emoji">🔗</div>
          </div>
          <span>LinkedIn</span>
        </a>
      </div>
    </div>

    <div class="desktop-right">
      <!-- Resume window (default) -->
      <div class="window" id="win-resume">
        <div class="window-header">
          <div class="window-title">RESUME // PROFILE.MSK</div>
          <div class="window-buttons">
            <span class="win-dot win-close"></span>
            <span class="win-dot win-min"></span>
            <span class="win-dot win-max"></span>
          </div>
        </div>
        <div class="win-body">
          <div class="win-body-inner">
            <div class="resume-grid">
              <div>
                <div class="resume-name">Madhugani Sai Kumar</div>
                <div class="resume-role">Python Developer · Full Stack · AI &amp; Blockchain</div>
                <p class="resume-about">
                  I am a B.Tech CSE student and Python developer who enjoys building real-world
                  systems: AI-powered tools, full stack web apps, and blockchain-backed platforms.
                  I focus on writing clean, maintainable code and delivering smooth user experiences.
                </p>

                <div class="resume-section-title">Core Skills</div>
                <ul class="resume-list">
                  <li>Python, FastAPI / Flask, Streamlit</li>
                  <li>JavaScript, basic React, REST APIs</li>
                  <li>SQL / NoSQL, authentication, JWT</li>
                  <li>AI / LLM integration, OCR, data parsing</li>
                </ul>
              </div>
              <div>
                <div class="resume-section-title">Education</div>
                <ul class="resume-list">
                  <li><b>B.Tech in Computer Science &amp; Engineering</b></li>
                  <li>2022 – Present</li>
                  <li>Focused on DSA, OS, DBMS, and software engineering.</li>
                </ul>

                <div class="resume-section-title">Status</div>
                <ul class="resume-list">
                  <li>Open to: Internships, project collabs, freelance dev</li>
                  <li>Location: India (remote-friendly)</li>
                </ul>

                <div class="resume-section-title">Contact</div>
                <ul class="resume-list">
                  <li>Email: <a href="mailto:your.email@example.com">your.email@example.com</a></li>
                  <li>GitHub: <a href="https://github.com/yourusername" target="_blank">github.com/yourusername</a></li>
                  <li>LinkedIn: <a href="https://linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/yourprofile</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Projects window -->
      <div class="window" id="win-projects">
        <div class="window-header">
          <div class="window-title">PROJECTS // DIR.MSK</div>
          <div class="window-buttons">
            <span class="win-dot win-close"></span>
            <span class="win-dot win-min"></span>
            <span class="win-dot win-max"></span>
          </div>
        </div>
        <div class="win-body">
          <div class="win-body-inner">
            <div class="project-card">
              <div class="project-tag">AI + Blockchain</div>
              <div class="project-title">ChainGuardian</div>
              <div class="project-desc">
                An AI-powered, blockchain-backed anti-fraud reputation system for e-commerce sellers.
                It aggregates on-chain signals, behavioral metrics, and trust scores to identify
                potentially fraudulent actors before they cause major damage.
              </div>
              <div class="project-tech">
                <span>Python</span>
                <span>Streamlit</span>
                <span>Smart Contracts</span>
                <span>IPFS</span>
              </div>
            </div>

            <div class="project-card">
              <div class="project-tag">AI / LLM</div>
              <div class="project-title">Medical Report Analyzer</div>
              <div class="project-desc">
                A pipeline that extracts values from medical PDFs using OCR + NLP, checks them against
                standard ranges, and generates simple explanations using LLMs so that patients and
                doctors can quickly understand key abnormalities.
              </div>
              <div class="project-tech">
                <span>Python</span>
                <span>OCR</span>
                <span>LLMs</span>
                <span>Streamlit</span>
              </div>
            </div>

            <div class="project-card">
              <div class="project-tag">Web / Portfolio</div>
              <div class="project-title">MSK Desktop Portfolio</div>
              <div class="project-desc">
                This interactive desktop-style hacker portfolio built entirely with Python &amp; Streamlit.
                It simulates a minimal OS with icons and windows, optimized for deployment on Streamlit Cloud.
              </div>
              <div class="project-tech">
                <span>Streamlit</span>
                <span>HTML · CSS</span>
                <span>Single-file App</span>
              </div>
            </div>

            <a href="#" class="close-link">Close window (go back)</a>
          </div>
        </div>
      </div>

      <!-- GitHub window -->
      <div class="window" id="win-github">
        <div class="window-header">
          <div class="window-title">GITHUB // REMOTE.MSK</div>
          <div class="window-buttons">
            <span class="win-dot win-close"></span>
            <span class="win-dot win-min"></span>
            <span class="win-dot win-max"></span>
          </div>
        </div>
        <div class="win-body">
          <div class="win-body-inner">
            <div class="link-block">
              <div class="link-label">GitHub Profile</div>
              <div class="link-main">
                Main account:
                <a href="https://github.com/yourusername" target="_blank">
                  github.com/yourusername
                </a>
              </div>
              <p style="margin-top:6px; font-size:12px;">
                Explore my code, experiments, and projects in Python, Streamlit, and AI.
              </p>
            </div>
            <a href="#" class="close-link" style="margin-top:8px; display:inline-block;">Close window (go back)</a>
          </div>
        </div>
      </div>

      <!-- LinkedIn window -->
      <div class="window" id="win-linkedin">
        <div class="window-header">
          <div class="window-title">LINKEDIN // NETWORK.MSK</div>
          <div class="window-buttons">
            <span class="win-dot win-close"></span>
            <span class="win-dot win-min"></span>
            <span class="win-dot win-max"></span>
          </div>
        </div>
        <div class="win-body">
          <div class="win-body-inner">
            <div class="link-block">
              <div class="link-label">LinkedIn Profile</div>
              <div class="link-main">
                Connect with me:
                <a href="https://linkedin.com/in/yourprofile" target="_blank">
                  linkedin.com/in/yourprofile
                </a>
              </div>
              <p style="margin-top:6px; font-size:12px;">
                Open to networking, internships, and interesting project collaborations
                around Python, AI, and full stack development.
              </p>
            </div>
            <a href="#" class="close-link" style="margin-top:8px; display:inline-block;">Close window (go back)</a>
          </div>
        </div>
      </div>

    </div> <!-- desktop-right -->
  </div> <!-- desktop -->

  <div class="taskbar">
    <div class="taskbar-left">
      <div class="taskbar-logo"></div>
      <span>MSK_DESKTOP</span>
    </div>
    <div class="taskbar-center">
      <div class="taskbar-pill">Resume.msk</div>
      <div class="taskbar-pill">Projects/</div>
    </div>
    <div class="taskbar-right">
      <span>PY 3.x</span>
      <span>STREAMLIT</span>
    </div>
  </div>
</div>
"""

st.markdown(html, unsafe_allow_html=True)
