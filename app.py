# app.py
from flask import Flask, send_from_directory, render_template_string, abort
import os
import pathlib

app = Flask(__name__, static_folder="static", template_folder="templates")

# -------------------------
# Edit this profile dict to your details
# -------------------------
profile = {
    "full_name": "Madhugani Sai Kumar",
    "first_name": "Madhugani",
    "title_line": "Full Stack Developer | ML & Web",
    "short_bio": "Building production-ready web apps and AI tools. Currently working on ChainGuardian (blockchain anti-fraud) and a Medical Report Analyzer.",
    "skills_line": "Python · JavaScript · React · Node.js · MongoDB · AWS",
    "email": "your.email@example.com",
    "location": "Indore, Madhya Pradesh, India",
    "response_time": "Within 24 hours",
    # path inside ./assets/ (make sure resume file exists there)
    "resume_filename": "resume.pdf",
    # socials: change URLs to your actual accounts
    "socials": {
        "instagram": "https://instagram.com/yourprofile",
        "linkedin": "https://linkedin.com/in/yourprofile",
        "github": "https://github.com/yourusername",
        "mailto": "mailto:your.email@example.com"
    },
    # Journey / timeline entries (will replace original timeline)
    "journey": [
        {
            "title": "Hackathon — ChainGuardian (lead)",
            "date": "July 2025",
            "desc": "Built an AI + blockchain anti-fraud reputation prototype for e-commerce sellers."
        },
        {
            "title": "Project — Medical Report Analyzer",
            "date": "Aug 2025",
            "desc": "Python + LLM pipeline for extracting and summarizing clinical reports."
        },
        {
            "title": "B.Tech — Computer Science",
            "date": "2022 - 2026",
            "desc": "Undergraduate studies focusing on full-stack development and AI."
        }
    ],
    # Projects / upcoming (simple examples)
    "upcoming_projects": [
        {"title": "Portfolio V2", "desc": "Rewritten with dynamic CMS and analytics"},
        {"title": "Open-source CLI", "desc": "Developer tooling for project scaffolding"}
    ]
}

# Utility: produce a blocks of HTML for the timeline from profile['journey']
def build_journey_html(journey_list):
    blocks = []
    for i, item in enumerate(journey_list):
        # alternate left/right for larger screens like original template
        side = "justify-end" if i % 2 == 0 else "justify-start"
        block = f'''
      <div class="relative mb-16 md:mb-24 md:flex {side}">
        <div class="hidden md:block absolute w-4 h-4 bg-[#1DCD9F] rounded-full left-1/2 transform -translate-x-1/2 top-4 z-10"></div>
        <div class="md:w-1/2"></div>
        <div class="md:w-1/2 md:pl-10">
          <div class="bg-[#111] p-6 rounded-2xl border border-[#1DCD9F] shadow-lg journey-card">
            <h3 class="text-xl font-semibold text-[#1DCD9F]">{item['title']}</h3>
            <span class="text-sm text-gray-400">{item['date']}</span>
            <p class="mt-2 text-gray-300">{item['desc']}</p>
          </div>
        </div>
      </div>
        '''
        # If left side instead of right, flip layout (small amount of HTML reuse is fine)
        if side == "justify-start":
            block = block.replace('<div class="md:w-1/2"></div>', '<div class="md:w-1/2 md:pr-10">', 1)
            block = block.replace('md:pl-10', 'md:pr-10')
        blocks.append(block)
    return "\n".join(blocks)

# Read original index.html (the one you uploaded) and perform string replacements.
# The original file contains hard-coded values (example: "Abhijeet Bhale", email, resume filename).
# We'll load it and do a set of safe replacements.
BASE_INDEX = "index.html"
if not os.path.exists(BASE_INDEX):
    raise FileNotFoundError(f"Could not find {BASE_INDEX}. Put your uploaded index.html next to app.py")

with open(BASE_INDEX, "r", encoding="utf-8") as f:
    original_html = f.read()

def transform_html(raw_html, profile):
    html = raw_html

    # Basic name/title/bio replacements
    html = html.replace("Abhijeet Bhale", profile["full_name"])
    html = html.replace(">Abhijeet<", f">{profile['first_name']}<")  # small hero button occurrences
    html = html.replace("An aspiring Full Stack Developer passionate about building sleek web\n      experiences.", profile["short_bio"])
    # update the <title>
    html = html.replace("<title>Portfolio / Abhijeet Bhale</title>", f"<title>Portfolio / {profile['full_name']}</title>")

    # replace bio paragraphs (common phrases)
    html = html.replace("I'm currently pursuing my B.Tech in Computer Science Engineering at\n        Medicaps University, Indore.", " ".join([profile["title_line"], profile["skills_line"]]))
    # replace skill highlights
    html = html.replace("JavaScript", "JavaScript")
    # email & download/resume
    html = html.replace("abhijeetbhale7@gmail.com", profile["email"])
    html = html.replace("Abhijeet Bhale Resume Updated 300925.pdf", profile["resume_filename"])
    # social links (examples in template)
    html = html.replace("https://www.instagram.com/isocyanideisgood?igsh=cDQ4NjEyeWFydDlp", profile["socials"]["instagram"])
    html = html.replace("https://www.linkedin.com/in/abhijeetbhale7?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", profile["socials"]["linkedin"])
    html = html.replace("https://github.com/abhijeetBhale", profile["socials"]["github"])
    html = html.replace("mailto:abhijeetbhale7@gmail.com", profile["socials"]["mailto"])

    # Replace hero letters loader (optional): set to first name initial letters
    initials_html = "".join([f'<span data-text="{c}">{c}</span>' for c in profile["first_name"].upper()])
    html = html.replace('<div class="loading-text" id="name-loader">', '<div class="loading-text" id="name-loader">', 1)
    # Naive replace: find the loader block start and end then replace contents.
    import re
    html = re.sub(r'(<div class="loading-text" id="name-loader">)[\s\S]*?(</div>)',
                  r'\1' + initials_html + r'\2', html, flags=re.MULTILINE)

    # Replace journey / timeline section content with our generated HTML
    journey_block = build_journey_html(profile["journey"])
    # Find the section with id="journey" and replace the inner container where cards were listed.
    html = re.sub(r'(<section id="journey"[\s\S]*?<div class="relative">)[\s\S]*?(</div>\s*</div>\s*</section>)',
                  r'\1\n' + journey_block + r'\n\2', html, flags=re.MULTILINE)

    # Replace upcoming projects area (a minimal implementation)
    if "upcoming_projects" in profile:
        up_blocks = []
        for p in profile["upcoming_projects"]:
            up_blocks.append(f'''
    <div class="upcoming-card bg-white text-black rounded-xl shadow-lg p-6">
      <h3 class="text-xl font-semibold mb-2">{p["title"]}</h3>
      <p class="text-gray-700 text-lg mb-4">{p["desc"]}</p>
      <span class="inline-block bg-yellow-100 text-yellow-700 px-3 py-1 rounded text-xs font-semibold">Coming Soon</span>
    </div>''')
        up_html = "\n".join(up_blocks)
        html = re.sub(r'(<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-10 max-w-6xl mx-auto">)[\s\S]*?(</div>\s*</section>)',
                      r'\1\n' + up_html + r'\n\2', html, flags=re.MULTILINE)

    return html

processed_html = transform_html(original_html, profile)

# Save processed template into templates/ so Flask can render it if we want dynamic rendering later
os.makedirs("templates", exist_ok=True)
with open(os.path.join("templates", "index_processed.html"), "w", encoding="utf-8") as f:
    f.write(processed_html)

# Ensure static folder exists; if your CSS/JS are at top-level, create static folder and copy them manually
# This app will serve from ./assets and ./static as-is.
@app.route("/")
def index():
    # render the processed HTML directly
    try:
        with open(os.path.join("templates", "index_processed.html"), "r", encoding="utf-8") as f:
            return render_template_string(f.read())
    except FileNotFoundError:
        abort(500, "Processed template not found")

# Serve assets (images, resume, icons) from ./assets
@app.route("/assets/<path:filename>")
def assets(filename):
    assets_dir = os.path.join(os.getcwd(), "assets")
    if os.path.exists(os.path.join(assets_dir, filename)):
        return send_from_directory(assets_dir, filename)
    else:
        abort(404)

# Serve static (if you move styles.css/script.js to ./static)
@app.route("/static/<path:filename>")
def static_files(filename):
    static_dir = os.path.join(os.getcwd(), "static")
    if os.path.exists(os.path.join(static_dir, filename)):
        return send_from_directory(static_dir, filename)
    else:
        # fallback: if file exists in root (original uploaded file), serve it
        if os.path.exists(os.path.join(os.getcwd(), filename)):
            return send_from_directory(os.getcwd(), filename)
        abort(404)

if __name__ == "__main__":
    # Run in debug mode for local testing
    app.run(host="0.0.0.0", port=5000, debug=True)
