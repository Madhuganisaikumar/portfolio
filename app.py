import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Madhugani Sai Kumar | Hacker Portfolio",
    page_icon="💻",
    layout="wide"
)

html = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Madhugani Sai Kumar | Hacker Portfolio</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: radial-gradient(circle at top, #050816 0%, #020617 40%, #000 100%);
      color: #e5e7eb;
      overflow-x: hidden;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    /* Matrix background */
    .matrix {
      position: fixed;
      inset: 0;
      z-index: -1;
      background: radial-gradient(circle at top, rgba(34,197,94,0.16), transparent 60%);
      overflow: hidden;
    }
    .matrix span {
      position: absolute;
      top: -10%;
      color: rgba(34,197,94,0.4);
      font-size: 14px;
      font-family: "Courier New", monospace;
      animation: fall linear infinite;
    }
    @keyframes fall {
      0%   { transform: translateY(-10vh); opacity: 0; }
      10%  { opacity: 0.7; }
      100% { transform: translateY(110vh); opacity: 0; }
    }

    .page {
      max-width: 1120px;
      margin: 0 auto;
      padding: 28px 16px 60px;
    }

    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 28px;
      gap: 16px;
    }

    .logo {
      font-family: "Courier New", monospace;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #22c55e;
      font-size: 18px;
    }

    nav {
      display: flex;
      gap: 16px;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #9ca3af;
    }

    nav a {
      position: relative;
      padding-bottom: 4px;
      cursor: pointer;
    }

    nav a::after {
      content: "";
      position: absolute;
      left: 0;
      bottom: 0;
      height: 2px;
      width: 0;
      background: linear-gradient(90deg, #22c55e, #38bdf8);
      transition: width 0.25s ease;
    }

    nav a:hover::after {
      width: 100%;
    }

    .hero {
      display: grid;
      grid-template-columns: minmax(0, 2fr) minmax(0, 1.4fr);
      gap: 24px;
      margin-bottom: 40px;
      align-items: center;
    }

    @media (max-width: 900px) {
      .hero {
        grid-template-columns: 1fr;
      }
    }

    .hero-text {
      opacity: 0;
      transform: translateY(16px);
      animation: fadeUp 0.9s ease-out forwards;
    }

    .eyebrow {
      font-size: 12px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #9ca3af;
      margin-bottom: 8px;
    }

    .glitch {
      font-size: 38px;
      font-weight: 800;
      letter-spacing: 0.04em;
      position: relative;
      color: #f9fafb;
    }

    @media (max-width: 600px) {
      .glitch { font-size: 30px; }
    }

    .glitch::before,
    .glitch::after {
      content: attr(data-text);
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      overflow: hidden;
      clip-path: inset(0 0 0 0);
    }

    .glitch::before {
      left: 1px;
      text-shadow: -1px 0 #22c55e;
      animation: glitch 2.4s infinite ease-in-out alternate;
    }

    .glitch::after {
      left: -1px;
      text-shadow: -1px 0 #38bdf8;
      animation: glitch 1.9s infinite ease-in-out alternate-reverse;
    }

    @keyframes glitch {
      0%   { clip-path: inset(10% 0 80% 0); }
      25%  { clip-path: inset(40% 0 30% 0); }
      50%  { clip-path: inset(80% 0 5% 0); }
      75%  { clip-path: inset(0 0 60% 0); }
      100% { clip-path: inset(20% 0 20% 0); }
    }

    .tagline {
      margin-top: 10px;
      font-size: 16px;
      color: #9ca3af;
    }

    .hero-desc {
      margin-top: 14px;
      font-size: 14px;
      color: #e5e7eb;
      line-height: 1.7;
      max-width: 520px;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 20px;
    }

    .btn-primary,
    .btn-outline {
      padding: 9px 18px;
      border-radius: 999px;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      cursor: pointer;
      border: 1px solid transparent;
    }

    .btn-primary {
      background: radial-gradient(circle at top left, #22c55e, #0f766e);
      color: #020617;
      font-weight: 700;
      box-shadow: 0 0 18px rgba(34,197,94,0.5);
    }

    .btn-primary:hover {
      filter: brightness(1.1);
      box-shadow: 0 0 24px rgba(34,197,94,0.7);
    }

    .btn-outline {
      border-color: rgba(148,163,184,0.7);
      background: rgba(15,23,42,0.9);
      color: #e5e7eb;
    }

    .btn-outline:hover {
      border-color: #22c55e;
    }

    .hero-meta {
      margin-top: 18px;
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      font-size: 12px;
      color: #9ca3af;
    }

    .hero-meta span {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .hero-meta span::before {
      content: "●";
      color: #22c55e;
      font-size: 8px;
    }

    .hero-right {
      position: relative;
      height: 230px;
      border-radius: 26px;
      padding: 16px;
      background: radial-gradient(circle at top left, #020617, #020617 55%, #000);
      border: 1px solid rgba(148,163,184,0.5);
      box-shadow: 0 20px 40px rgba(15,23,42,0.95);
      overflow: hidden;
      opacity: 0;
      transform: translateY(20px);
      animation: fadeUp 0.9s ease-out 0.12s forwards;
    }

    .scan {
      position: absolute;
      inset: 0;
      background-image: linear-gradient(
        to bottom,
        rgba(15,23,42,0.2) 1px,
        transparent 1px
      );
      background-size: 100% 3px;
      mix-blend-mode: soft-light;
      pointer-events: none;
    }

    .hud-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #9ca3af;
      margin-bottom: 10px;
    }

    .hud-dots {
      display: flex;
      gap: 4px;
    }

    .hud-dot {
      width: 7px;
      height: 7px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 8px rgba(34,197,94,0.7);
    }
    .hud-dot:nth-child(2){ background:#facc15; box-shadow:0 0 8px rgba(250,204,21,0.7);}
    .hud-dot:nth-child(3){ background:#fb923c; box-shadow:0 0 8px rgba(251,146,60,0.7);}

    .hud-main {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 10px;
      font-size: 12px;
    }

    .hud-name {
      font-size: 16px;
      font-weight: 600;
      color: #f9fafb;
      margin-bottom: 4px;
    }

    .hud-role {
      font-size: 12px;
      color: #a5b4fc;
      margin-bottom: 10px;
    }

    .hud-row {
      display: flex;
      justify-content: space-between;
      color: #9ca3af;
      margin-bottom: 4px;
    }

    .hud-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }

    .hud-tag {
      padding: 3px 7px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.7);
      background: rgba(15,23,42,0.95);
      font-size: 10px;
    }

    .hud-side {
      border-radius: 16px;
      border: 1px dashed rgba(148,163,184,0.7);
      padding: 9px;
      background: radial-gradient(circle at top, rgba(34,197,94,0.15), transparent);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .hud-side-title {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #9ca3af;
    }

    .hud-side-line {
      height: 1px;
      background: linear-gradient(90deg, transparent, #22c55e, transparent);
      opacity: 0.7;
    }

    .hud-side p {
      font-size: 11px;
      color: #e5e7eb;
      line-height: 1.5;
    }

    .hud-pill {
      margin-top: 4px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 3px 9px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.7);
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.14em;
    }

    .hud-pill-dot {
      width: 8px;
      height: 8px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 10px rgba(34,197,94,0.9);
    }

    .hud-bottom {
      position: absolute;
      inset-inline: 16px;
      bottom: 10px;
      display: flex;
      justify-content: space-between;
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #9ca3af;
    }

    .signal {
      width: 10px;
      height: 10px;
      border-radius: 999px;
      border: 1px solid rgba(34,197,94,0.7);
      box-shadow: 0 0 10px rgba(34,197,94,0.7);
      position: relative;
    }

    .signal::after {
      content: "";
      position: absolute;
      inset: 3px;
      border-radius: inherit;
      background: #22c55e;
    }

    section {
      margin-bottom: 34px;
      opacity: 0;
      transform: translateY(18px);
      animation: fadeUp 0.9s ease-out forwards;
    }

    section:nth-of-type(1){ animation-delay:0.16s;}
    section:nth-of-type(2){ animation-delay:0.22s;}
    section:nth-of-type(3){ animation-delay:0.28s;}
    section:nth-of-type(4){ animation-delay:0.34s;}

    .section-title {
      font-size: 16px;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      color: #9ca3af;
      margin-bottom: 14px;
    }
    .section-title span { color: #22c55e; }

    .skills-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
    }

    .skill-card {
      border-radius: 16px;
      padding: 10px 12px 12px;
      background: radial-gradient(circle at top left, rgba(34,197,94,0.16), rgba(15,23,42,0.9));
      border: 1px solid rgba(148,163,184,0.7);
      box-shadow: 0 14px 30px rgba(15,23,42,1);
    }

    .skill-header {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      margin-bottom: 4px;
    }

    .skill-name { font-weight: 500; }
    .skill-val { font-size: 12px; color:#9ca3af; }

    .skill-bar {
      position: relative;
      height: 7px;
      border-radius: 999px;
      background: rgba(15,23,42,0.95);
      border: 1px solid rgba(31,41,55,0.9);
      overflow: hidden;
    }

    .skill-fill {
      position: absolute;
      inset: 0;
      transform-origin: left;
      transform: scaleX(0);
      border-radius: inherit;
      background: linear-gradient(90deg, #22c55e, #38bdf8);
      box-shadow: 0 0 16px rgba(34,197,94,0.7);
      animation: load 1.2s ease-out forwards;
    }

    .skill-fill[data-lvl="92"] { animation-delay:0.05s; transform:scaleX(0.92); }
    .skill-fill[data-lvl="88"] { animation-delay:0.1s;  transform:scaleX(0.88); }
    .skill-fill[data-lvl="85"] { animation-delay:0.15s; transform:scaleX(0.85); }
    .skill-fill[data-lvl="82"] { animation-delay:0.2s;  transform:scaleX(0.82); }
    .skill-fill[data-lvl="80"] { animation-delay:0.25s; transform:scaleX(0.80); }

    @keyframes load {
      from { transform: scaleX(0); }
    }

    .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 14px;
    }

    .project {
      position: relative;
      border-radius: 18px;
      padding: 13px 13px 12px;
      background: radial-gradient(circle at top, rgba(15,23,42,0.96), #020617);
      border: 1px solid rgba(148,163,184,0.7);
      box-shadow: 0 16px 36px rgba(15,23,42,1);
      overflow: hidden;
    }

    .project::before {
      content: "";
      position: absolute;
      inset: -30%;
      background: radial-gradient(circle at top left, rgba(34,197,94,0.26), transparent 60%);
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .project:hover::before { opacity: 1; }

    .project-tag {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #9ca3af;
      margin-bottom: 6px;
    }

    .project-title {
      font-size: 17px;
      font-weight: 600;
      margin-bottom: 6px;
      color: #f9fafb;
    }

    .project-desc {
      font-size: 13px;
      color: #d1d5db;
      line-height: 1.6;
      margin-bottom: 8px;
    }

    .project-tech {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      font-size: 11px;
      color: #9ca3af;
      margin-bottom: 4px;
    }

    .project-tech span {
      padding: 3px 7px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.7);
      background: rgba(15,23,42,0.9);
    }

    .project-status {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      color: #22c55e;
    }

    .status-dot {
      width: 7px;
      height: 7px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 12px rgba(34,197,94,0.9);
    }

    .journey {
      border-radius: 18px;
      padding: 12px 13px;
      background: radial-gradient(circle at top, rgba(15,23,42,0.98), #020617);
      border: 1px solid rgba(148,163,184,0.7);
      box-shadow: 0 16px 38px rgba(15,23,42,1);
    }

    .journey-item {
      display: flex;
      gap: 10px;
      padding: 9px 0;
      border-bottom: 1px dashed rgba(55,65,81,0.9);
    }

    .journey-item:last-child { border-bottom: none; }

    .j-dot {
      width: 9px;
      height: 9px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 14px rgba(34,197,94,0.9);
      margin-top: 6px;
    }

    .j-title {
      font-size: 14px;
      color: #f9fafb;
      margin-bottom: 2px;
    }

    .j-time {
      font-size: 11px;
      color: #9ca3af;
      margin-bottom: 2px;
    }

    .j-desc {
      font-size: 13px;
      color: #d1d5db;
    }

    .contact {
      border-radius: 18px;
      padding: 12px 13px;
      background: radial-gradient(circle at top, rgba(15,23,42,0.97), #020617);
      border: 1px solid rgba(148,163,184,0.7);
      box-shadow: 0 16px 36px rgba(15,23,42,1);
      font-size: 13px;
      color: #d1d5db;
    }

    .contact-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 8px;
    }

    .contact-label {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #9ca3af;
      margin-bottom: 4px;
    }

    .contact-link {
      padding: 4px 9px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.7);
      background: rgba(15,23,42,0.95);
      font-size: 12px;
    }

    .contact-link:hover {
      border-color: #22c55e;
    }

    footer {
      margin-top: 18px;
      text-align: center;
      font-size: 11px;
      color: #6b7280;
    }
    footer span { color:#22c55e; }

    @keyframes fadeUp {
      to { opacity:1; transform:translateY(0); }
    }
  </style>
</head>
<body>
  <div class="matrix" id="matrix"></div>

  <div class="page">
    <header>
      <div class="logo">MSK_</div>
      <nav>
        <a href="#top">Home</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#journey">Journey</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>

    <main id="top">
      <div class="hero">
        <div class="hero-text">
          <div class="eyebrow">PORTFOLIO // HACKER MODE</div>
          <h1 class="glitch" data-text="Madhugani Sai Kumar">Madhugani Sai Kumar</h1>
          <p class="tagline">Python Developer · Full Stack · AI &amp; Blockchain</p>
          <p class="hero-desc">
            I build intelligent, high-performance systems — from AI-driven medical analyzers
            to blockchain-based fraud detection engines. I love clean dark UIs, fast backends,
            and real-world problem solving.
          </p>
          <div class="hero-actions">
            <a href="#projects" class="btn-primary">VIEW PROJECTS</a>
            <a href="#contact" class="btn-outline">CONTACT ME</a>
          </div>
          <div class="hero-meta">
            <span>Based in India</span>
            <span>Available for internships &amp; collabs</span>
            <span>Response time: &lt; 24 hours</span>
          </div>
        </div>

        <aside class="hero-right">
          <div class="scan"></div>
          <div class="hud-top">
            <span>// SYSTEM STATUS</span>
            <div class="hud-dots">
              <div class="hud-dot"></div>
              <div class="hud-dot"></div>
              <div class="hud-dot"></div>
            </div>
          </div>
          <div class="hud-main">
            <div>
              <div class="hud-name">Madhugani S. Kumar</div>
              <div class="hud-role">Python · Full Stack · AI &amp; Blockchain</div>
              <div class="hud-row">
                <span>Primary Stack</span>
                <span>Python · JS · SQL</span>
              </div>
              <div class="hud-row">
                <span>Tools</span>
                <span>Streamlit · Flask</span>
              </div>
              <div class="hud-tags">
                <div class="hud-tag">ChainGuardian</div>
                <div class="hud-tag">Medical Report Analyzer</div>
                <div class="hud-tag">LLM Apps</div>
              </div>
            </div>
            <div class="hud-side">
              <div class="hud-side-title">Runtime Snapshot</div>
              <div class="hud-side-line"></div>
              <p>B.Tech CSE student building projects in AI, blockchain, and full stack web.</p>
              <div class="hud-pill">
                <div class="hud-pill-dot"></div>
                ACTIVE // CODING SESSION
              </div>
            </div>
          </div>
          <div class="hud-bottom">
            <span><div class="signal"></div> ONLINE</span>
            <span>PORT 8501 / STREAMLIT</span>
          </div>
        </aside>
      </div>

      <section id="skills">
        <div class="section-title"><span>01</span> // Skills &amp; Stack</div>
        <div class="skills-grid">
          <div class="skill-card">
            <div class="skill-header">
              <span class="skill-name">Python &amp; Backend</span>
              <span class="skill-val">92%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-fill" data-lvl="92"></div>
            </div>
          </div>

          <div class="skill-card">
            <div class="skill-header">
              <span class="skill-name">Streamlit &amp; Flask</span>
              <span class="skill-val">88%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-fill" data-lvl="88"></div>
            </div>
          </div>

          <div class="skill-card">
            <div class="skill-header">
              <span class="skill-name">JavaScript &amp; Frontend</span>
              <span class="skill-val">85%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-fill" data-lvl="85"></div>
            </div>
          </div>

          <div class="skill-card">
            <div class="skill-header">
              <span class="skill-name">AI / LLM Integration</span>
              <span class="skill-val">82%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-fill" data-lvl="82"></div>
            </div>
          </div>

          <div class="skill-card">
            <div class="skill-header">
              <span class="skill-name">Databases &amp; APIs</span>
              <span class="skill-val">80%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-fill" data-lvl="80"></div>
            </div>
          </div>
        </div>
      </section>

      <section id="projects">
        <div class="section-title"><span>02</span> // Featured Projects</div>
        <div class="projects-grid">
          <article class="project">
            <div class="project-tag">AI + Blockchain</div>
            <div class="project-title">ChainGuardian</div>
            <p class="project-desc">
              AI-powered, blockchain-backed anti-fraud reputation system for e-commerce sellers.
              Tracks on-chain signals, behavior, and trust scores to flag suspicious activity.
            </p>
            <div class="project-tech">
              <span>Python</span>
              <span>Streamlit</span>
              <span>Smart Contracts</span>
              <span>IPFS</span>
            </div>
            <div class="project-status">
              <div class="status-dot"></div>
              In active development
            </div>
          </article>

          <article class="project">
            <div class="project-tag">AI / LLM</div>
            <div class="project-title">Medical Report Analyzer</div>
            <p class="project-desc">
              Extracts and interprets values from medical PDFs using OCR + LLMs, compares them
              to normal ranges, and generates simple summaries for patients and doctors.
            </p>
            <div class="project-tech">
              <span>Python</span>
              <span>OCR</span>
              <span>LLMs</span>
              <span>Streamlit</span>
            </div>
            <div class="project-status">
              <div class="status-dot"></div>
              Prototype ready
            </div>
          </article>

          <article class="project">
            <div class="project-tag">Web / Portfolio</div>
            <div class="project-title">Hacker Portfolio</div>
            <p class="project-desc">
              This neon, matrix-style portfolio built as a single Python + Streamlit file with
              animated HUD, loading bars, and cyberpunk UI.
            </p>
            <div class="project-tech">
              <span>Streamlit</span>
              <span>HTML · CSS · JS</span>
            </div>
            <div class="project-status">
              <div class="status-dot"></div>
              Deployed on Streamlit Cloud
            </div>
          </article>
        </div>
      </section>

      <section id="journey">
        <div class="section-title"><span>03</span> // Journey</div>
        <div class="journey">
          <div class="journey-item">
            <div class="j-dot"></div>
            <div>
              <div class="j-title">B.Tech in Computer Science &amp; Engineering</div>
              <div class="j-time">2022 – Present</div>
              <div class="j-desc">
                Building strong fundamentals in algorithms, data structures, OS, networking,
                and software engineering.
              </div>
            </div>
          </div>
          <div class="journey-item">
            <div class="j-dot"></div>
            <div>
              <div class="j-title">ChainGuardian (Hackathon project)</div>
              <div class="j-time">2025</div>
              <div class="j-desc">
                Led the development of an AI + blockchain prototype for fraud detection in
                e-commerce, from concept to working demo.
              </div>
            </div>
          </div>
          <div class="journey-item">
            <div class="j-dot"></div>
            <div>
              <div class="j-title">Medical Report Analyzer</div>
              <div class="j-time">2025</div>
              <div class="j-desc">
                Built an LLM-powered tool that understands real diagnostic reports and
                highlights abnormal values with plain-language explanations.
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="contact">
        <div class="section-title"><span>04</span> // Contact &amp; Links</div>
        <div class="contact">
          <div class="contact-label">Message</div>
          <p>
            Want to collaborate or need a Python / AI / web dev for your idea?
            Drop a mail or ping me on GitHub / LinkedIn.
          </p>
          <div class="contact-row">
            <div>
              <div class="contact-label">Email</div>
              <a class="contact-link" href="mailto:your.email@example.com">
                your.email@example.com
              </a>
            </div>
            <div>
              <div class="contact-label">GitHub</div>
              <a class="contact-link" href="https://github.com/yourusername" target="_blank">
                github.com/yourusername
              </a>
            </div>
            <div>
              <div class="contact-label">LinkedIn</div>
              <a class="contact-link" href="https://linkedin.com/in/yourprofile" target="_blank">
                linkedin.com/in/yourprofile
              </a>
            </div>
          </div>
        </div>
      </section>

      <footer>
        © 2025 <span>Madhugani Sai Kumar</span> — built as a single-file Python / Streamlit hacker portfolio.
      </footer>
    </main>
  </div>

  <script>
    // Matrix rain
    const matrix = document.getElementById("matrix");
    const chars = "01MSK<>[]{}AI";
    function spawnSymbol() {
      const span = document.createElement("span");
      span.textContent = chars[Math.floor(Math.random() * chars.length)];
      span.style.left = Math.random() * window.innerWidth + "px";
      span.style.animationDuration = 4 + Math.random() * 4 + "s";
      span.style.fontSize = 10 + Math.random() * 8 + "px";
      matrix.appendChild(span);
      setTimeout(() => matrix.removeChild(span), 9000);
    }
    for (let i = 0; i < 70; i++) {
      setTimeout(spawnSymbol, i * 120);
    }
    setInterval(spawnSymbol, 160);
  </script>
</body>
</html>
"""

