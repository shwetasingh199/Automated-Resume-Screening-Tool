import streamlit as st
import pandas as pd
import tempfile
import plotly.express as px

from src.extractor import extract_text
from src.cleaner import clean_text
from src.advanced_matcher import analyze_skills
from src.scorer import calculate_similarity
from src.matcher import extract_skills

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening Tool",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("📄 AI-Powered Resume Screening Tool")

st.markdown("""
This ATS-style platform screens resumes using:
- NLP
- Sentence Transformers
- Semantic Similarity
- Skill Matching
- AI Resume Ranking
""")

# ---------------------------------------------------
# SIDEBAR CONTROLS
# ---------------------------------------------------

st.sidebar.title("⚙️ ATS Controls")

minimum_score = st.sidebar.slider(
    "Minimum ATS Score",
    min_value=0,
    max_value=100,
    value=60
)

show_only_shortlisted = st.sidebar.checkbox(
    "Show Only Shortlisted Candidates"
)

# ---------------------------------------------------
# LOAD JOB DESCRIPTION
# ---------------------------------------------------

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

job_description_clean = clean_text(job_description)

# ---------------------------------------------------
# LOAD REQUIRED SKILLS
# ---------------------------------------------------

with open("data/required_skills.txt", "r", encoding="utf-8") as file:
    skills_list = [
        line.strip()
        for line in file.readlines()
    ]

# ---------------------------------------------------
# DISPLAY JOB DESCRIPTION
# ---------------------------------------------------

st.subheader("📌 Job Description")

edited_jd = st.text_area(
    "Edit Job Description",
    value=job_description,
    height=250
)

job_description_clean = clean_text(edited_jd)

# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------

st.subheader("📤 Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF / DOCX / TXT resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# ---------------------------------------------------
# PROCESS RESUMES
# ---------------------------------------------------

results = []

if uploaded_files:

    progress_bar = st.progress(0)

    for index, uploaded_file in enumerate(uploaded_files):

        # -------------------------------------------
        # SAVE TEMP FILE
        # -------------------------------------------

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix="." + uploaded_file.name.split(".")[-1]
        ) as temp_file:

            temp_file.write(uploaded_file.read())

            temp_path = temp_file.name

        # -------------------------------------------
        # EXTRACT TEXT
        # -------------------------------------------

        resume_text = extract_text(temp_path)

        # -------------------------------------------
        # CLEAN TEXT
        # -------------------------------------------

        cleaned_resume = clean_text(resume_text)

        # -------------------------------------------
        # SKILL EXTRACTION
        # -------------------------------------------

        matched_skills = extract_skills(
            cleaned_resume,
            skills_list
        )

        # -------------------------------------------
        # SKILL ANALYSIS
        # -------------------------------------------

        analysis = analyze_skills(
            matched_skills,
            skills_list
        )

        missing_skills = analysis["missing"]

        match_percentage = analysis[
            "match_percentage"
        ]

        # -------------------------------------------
        # AI SIMILARITY SCORE
        # -------------------------------------------

        score = calculate_similarity(
            job_description_clean,
            cleaned_resume
        )

        # -------------------------------------------
        # ATS DECISION
        # -------------------------------------------

        if score >= 80:
            decision = "Highly Recommended"

        elif score >= minimum_score:
            decision = "Shortlisted"

        elif score >= 40:
            decision = "Consider"

        else:
            decision = "Rejected"

        # -------------------------------------------
        # STORE RESULTS
        # -------------------------------------------

        results.append({

            "Resume Name":
                uploaded_file.name,

            "Matched Skills":
                ", ".join(matched_skills),

            "Missing Skills":
                ", ".join(missing_skills),

            "Skill Match %":
                match_percentage,

            "ATS Score":
                score,

            "Decision":
                decision
        })

        # UPDATE PROGRESS BAR
        progress_bar.progress(
            (index + 1) / len(uploaded_files)
        )

    # ---------------------------------------------------
    # CREATE DATAFRAME
    # ---------------------------------------------------

    df = pd.DataFrame(results)

    # SORT BY SCORE
    df = df.sort_values(
        by="ATS Score",
        ascending=False
    )

    # ---------------------------------------------------
    # FILTER SHORTLISTED
    # ---------------------------------------------------

    if show_only_shortlisted:

        df = df[
            df["Decision"].isin(
                [
                    "Highly Recommended",
                    "Shortlisted"
                ]
            )
        ]

    # ---------------------------------------------------
    # SHOW RESULTS
    # ---------------------------------------------------

    st.subheader("📊 Resume Screening Results")

    st.dataframe(
        df,
        use_container_width=True
    )

    # ---------------------------------------------------
    # ANALYTICS
    # ---------------------------------------------------

    st.subheader("📈 Resume Score Analytics")

    fig = px.bar(
        df,
        x="Resume Name",
        y="ATS Score",
        color="Decision",
        text="ATS Score",
        title="Candidate Ranking Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------------------------------------------
    # PIE CHART
    # ---------------------------------------------------

    st.subheader("📌 Candidate Distribution")

    pie_chart = px.pie(
        df,
        names="Decision",
        title="Screening Decisions"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    # ---------------------------------------------------
    # TOP CANDIDATE
    # ---------------------------------------------------

    st.subheader("🏆 Top Candidate")

    top_candidate = df.iloc[0]

    st.success(
        f"""
        Best Match: {top_candidate['Resume Name']}

        ATS Score: {top_candidate['ATS Score']}

        Decision: {top_candidate['Decision']}
        """
    )

    # ---------------------------------------------------
    # DOWNLOAD CSV
    # ---------------------------------------------------

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download Screening Report",
        data=csv,
        file_name="screening_results.csv",
        mime="text/csv"
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown("""
### 🚀 Features
- Dynamic Resume Upload
- AI Semantic Matching
- ATS Scoring
- Skill Gap Analysis
- Resume Ranking
- Interactive Analytics
- CSV Export
""")