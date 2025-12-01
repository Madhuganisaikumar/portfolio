import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Madhugani Sai Kumar | Hacker Portfolio",
    page_icon="💻",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Madhugani Sai Kumar | Hacker Portfolio</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>

    /* ===== RESET ===== */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text",
        "Segoe UI", sans-serif;
      background: radial-gradient(circle at top, #071b2c 0%, #020309 45%, #000 100%);
      color: #f5f5f5;
      overflow-x: hidden;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    /* ===== MATRIX BACKGROUND ===== */
    .matrix {
      position: fixed;
      inset: 0;
      z-index: -1;
      background: radial-gradient(circle at top, rgba(0,255,170,0.08), transparent 60%);
      overflow: hidden;
    }

    .matrix span {
      position: absolute;
      top: -10%;
      color: rgba(0, 255, 170, 0.25);
      font-size: 14px;
      font-family: "Courier New", monospace;
      animation: fall linear infinite;
      opacity: 0.4;
    }

    @keyframes fall {
      0% { transform: translateY(-10vh); opacity: 0; }
      10% { opacity: 0.6; }
      100% { transform: translateY(110vh); opacity: 0; }
    }

    /* ===== LAYOUT ===== */
    .page {
      max-width: 1200px;
      margin: 0 auto;
      padding: 32px 18px 64px;
    }

    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 40px;
    }

    .logo {
      font-family: "Courier New", monospace;
      font-size: 20px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #1dcd9f;
    }

    nav {
      display: flex;
      gap: 18px;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #b7b7b7;
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
      width: 0;
      height: 2px;
      background: linear-gradient(90deg, #1dcd9f, #38bdf8);
      transition: width 0.3s ease;
    }

    nav a:hover::after {
      width: 100%;
    }

    /* ===== HERO SECTION ===== */
    .hero {
      display: grid;
      grid-template-columns: minmax(0, 2fr) minmax(0, 1.4fr);
      gap: 28px;
      margin-bottom: 48px;
      align-items: center;
    }

    @media (max-width: 900px) {
      .hero {
        grid-template-columns: 1fr;
      }
    }

    .hero-text {
      animation: fadeUp 0.9s ease-out forwards;
      opacity: 0;
      transform: translateY(14px);
    }

    .eyebrow {
      font-size: 13px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #9ca3af;
      margin-bottom: 10px;
    }

    .glitch {
      font-size: 42px;
      font-weight: 800;
      letter-spacing: 0.03em;
      position: relative;
      color: #e5e7eb;
      text-shadow: 0 0 6px rgba(0, 0, 0, 0.8);
    }

    @media (max-width: 600px) {
      .glitch {
        font-size: 32px;
      }
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
      animation: glitch 2.7s infinite ease-in-out alternate-reverse;
    }

    .glitch::after {
      left: -1px;
      text-shadow: -1px 0 #38bdf8;
      animation: glitch 2.2s infinite ease-in-out alternate;
    }

    @keyframes glitch {
      0% { clip-path: inset(0 0 90% 0); }
      10% { clip-path: inset(10% 0 55% 0); }
      20% { clip-path: inset(80% 0 5% 0); }
      30% { clip-path: inset(0 0 80% 0); }
      40% { clip-path: inset(45% 0 10% 0); }
      50% { clip-path: inset(80% 0 0 0); }
      60% { clip-path: inset(5% 0 80% 0); }
      70% { clip-path: inset(0 0 30% 0); }
      80% { clip-path: inset(10% 0 50% 0); }
      90% { clip-path: inset(40% 0 20% 0); }
      100% { clip-path: inset(0 0 100% 0); }
    }

    .tagline {
      font-size: 18px;
      margin-top: 10px;
      color: #9ca3af;
    }

    .hero-desc {
      margin-top: 16px;
      line-height: 1.6;
      font-size: 15px;
      color: #e5e7eb;
      max-width: 560px;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 22px;
    }

    .btn-primary,
    .btn-ghost {
      padding: 10px 18px;
      border-radius: 999px;
      font-size: 14px;
      border: 1px solid transparent;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }

    .btn-primary {
      background: radial-gradient(circle at top left, #22c55e, #0f766e);
      box-shadow: 0 0 18px rgba(34, 197, 94, 0.35);
      color: #0b1120;
      font-weight: 700;
    }

    .btn-primary:hover {
      filter: brightness(1.08);
      box-shadow: 0 0 30px rgba(34, 197, 94, 0.55);
    }

    .btn-ghost {
      border-color: rgba(148, 163, 184, 0.7);
      color: #e5e7eb;
      background: rgba(15, 23, 42, 0.8);
    }

    .btn-ghost:hover {
      background: rgba(15, 23, 42, 0.9);
      border-color: #22c55e;
    }

    .hero-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 18px;
      margin-top: 18px;
      font-size: 13px;
      color: #9ca3af;
    }

    .hero-meta span {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .hero-meta span::before {
      content: "●";
      font-size: 8px;
      color: #22c55e;
    }

    /* ===== HERO SIDEBAR (RIGHT) ===== */
    .hero-right {
      position: relative;
      height: 260px;
      border-radius: 32px;
      padding: 20px;
      background: radial-gradient(circle at top left, #0f172a, #020617);
      border: 1px solid rgba(148, 163, 184, 0.4);
      box-shadow: 0 22px 50px rgba(15, 23, 42, 0.95);
      overflow: hidden;
      animation: fadeUp 1s ease-out forwards;
      opacity: 0;
      transform: translateY(18px);
      animation-delay: 0.12s;
    }

    .scan-lines {
      position: absolute;
      inset: 0;
      background-image: linear-gradient(
        to bottom,
        rgba(15, 23, 42, 0.25) 1px,
        transparent 1px
      );
      background-size: 100% 3px;
      opacity: 0.7;
      pointer-events: none;
      mix-blend-mode: soft-light;
    }

    .hud-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: #9ca3af;
      margin-bottom: 14px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
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
      box-shadow: 0 0 7px rgba(34, 197, 94, 0.6);
    }

    .hud-dot:nth-child(2) {
      background: #facc15;
      box-shadow: 0 0 7px rgba(250, 204, 21, 0.5);
    }

    .hud-dot:nth-child(3) {
