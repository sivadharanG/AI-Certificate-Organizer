import streamlit as st
import pytesseract
from PIL import Image
import pdfplumber
import re
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

# --------------------------------------
# GEMINI CLIENT
# --------------------------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# --------------------------------------
# PAGE CONFIG
# --------------------------------------
st.set_page_config(
    page_title="AI Certificate Organizer",
    layout="wide"
)

# --------------------------------------
# TESSERACT PATH
# --------------------------------------
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# --------------------------------------
# SKILL DATABASE
# --------------------------------------
skills = {
    "python": "Programming",
    "artificial intelligence": "AI",
    "machine learning": "AI",
    "deep learning": "AI",
    "nlp": "AI",
    "data science": "Data",
    "computer vision": "AI",
    "prompt engineering": "Generative AI",
    "generative ai": "Generative AI",
    "openai": "Generative AI",
    "tensorflow": "AI",
    "streamlit": "Web Development",
    "pandas": "Data",
    "numpy": "Data",
}

# --------------------------------------
# SIDEBAR
# --------------------------------------
st.sidebar.title("🎓 AI Certificate Organizer")

st.sidebar.info(
    "Upload certificates and analyze your skills automatically."
)

# --------------------------------------
# TITLE
# --------------------------------------
st.title("🚀 Advanced AI Certificate Organizer")

st.write(
    "Upload certificate images or PDFs for AI-based analysis."
)

# --------------------------------------
# FILE UPLOADER
# --------------------------------------
uploaded_files = st.file_uploader(
    "Upload Certificates",
    type=["png", "jpg", "jpeg", "pdf"],
    accept_multiple_files=True
)

# --------------------------------------
# MAIN PROCESS
# --------------------------------------
if uploaded_files:

    all_detected_skills = []
    all_categories = []

    st.success("Certificates uploaded successfully!")

    extracted_all_text = ""

    # ----------------------------------
    # PROCESS EACH FILE
    # ----------------------------------
    for file in uploaded_files:

        extracted_text = ""

        # PDF PROCESSING
        if file.type == "application/pdf":

            st.write(f"📄 PDF Uploaded: {file.name}")

            with pdfplumber.open(file) as pdf:

                for page in pdf.pages:

                    text = page.extract_text()

                    if text:
                        extracted_text += text

        # IMAGE PROCESSING
        else:

            image = Image.open(file)

            st.image(image, width=250)

            extracted_text = pytesseract.image_to_string(image)

        extracted_all_text += extracted_text.lower()

    # ----------------------------------
    # SKILL DETECTION
    # ----------------------------------
    for skill, category in skills.items():

        if re.search(skill, extracted_all_text):

            all_detected_skills.append(skill)
            all_categories.append(category)

    # Remove duplicates
    unique_skills = list(set(all_detected_skills))
    unique_categories = list(set(all_categories))

    # ----------------------------------
    # DASHBOARD
    # ----------------------------------
    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Certificates", len(uploaded_files))
    col2.metric("Skills", len(unique_skills))
    col3.metric("Domains", len(unique_categories))

    # ----------------------------------
    # DETECTED SKILLS
    # ----------------------------------
    st.subheader("🧠 Skills Detected")

    for skill in unique_skills:
        st.success(skill.title())

    # ----------------------------------
    # CATEGORY ANALYSIS
    # ----------------------------------
    st.subheader("📂 Domain Analysis")

    category_count = Counter(all_categories)

    category_df = pd.DataFrame({
        "Domain": category_count.keys(),
        "Count": category_count.values()
    })

    st.dataframe(category_df)

    # ----------------------------------
    # SKILL CHART
    # ----------------------------------
    st.subheader("📈 Skill Frequency Chart")

    skill_count = Counter(all_detected_skills)

    fig, ax = plt.subplots()

    ax.bar(
        skill_count.keys(),
        skill_count.values()
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

    # ----------------------------------
    # LINKEDIN CAPTION
    # ----------------------------------
    prompt = f"""
Generate a professional LinkedIn post for someone who completed certifications in:
{', '.join(unique_skills)}

Make it professional, motivational, and beginner friendly.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    linkedin_caption = response.text

    st.subheader("📢 AI LinkedIn Caption")

    st.write(linkedin_caption)

    # ----------------------------------
    # RESUME SUMMARY
    # ----------------------------------
    st.subheader("💼 Resume Summary")

    resume_summary = f"""
Skilled in {', '.join(unique_skills)} through certifications,
projects, and practical learning experiences.
"""

    st.code(resume_summary)

    # ----------------------------------
    # CAREER RECOMMENDATIONS
    # ----------------------------------
    st.subheader("🚀 Career Recommendations")

    if "machine learning" in unique_skills:
        st.info("➡ Recommended Role: Machine Learning Engineer")

    if "data science" in unique_skills:
        st.info("➡ Recommended Role: Data Analyst / Data Scientist")

    if "generative ai" in unique_skills:
        st.info("➡ Recommended Role: Generative AI Developer")

    if "python" in unique_skills:
        st.info("➡ Recommended Next Skill: Flask or FastAPI")

    # ----------------------------------
    # AI READINESS SCORE
    # ----------------------------------
    st.subheader("🎯 AI Readiness Score")

    score = len(unique_skills) * 10

    if score > 100:
        score = 100

    st.progress(score)

    st.write(f"AI Readiness Score: {score}/100")

else:
    st.warning("Upload certificates to begin analysis.")