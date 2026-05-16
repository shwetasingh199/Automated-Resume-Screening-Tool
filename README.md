# 📄 AI-Powered Automated Resume Screening Tool

An industry-oriented ATS (Applicant Tracking System) Resume Screening Platform built using Python, NLP, Sentence Transformers, and Streamlit.

This project simulates how modern HR Tech platforms automatically screen, rank, and shortlist resumes based on job descriptions, required skills, semantic similarity, and AI-powered matching.

---

# 🚀 Project Overview

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing each resume is time-consuming and inefficient.

This project automates the resume screening workflow by:

* Parsing resumes (PDF/DOCX/TXT)
* Extracting text and skills
* Comparing resumes with job descriptions
* Calculating ATS scores using AI semantic matching
* Identifying missing skills
* Ranking candidates automatically
* Generating downloadable reports

The system behaves like a real-world ATS platform used by HR teams and recruitment companies.

---

# 🎯 Industry Relevance

This project demonstrates concepts used in:

* HR Tech Platforms
* ATS Software
* AI Recruitment Systems
* Resume Intelligence Systems
* NLP-based Screening Engines

It is highly relevant for:

* Python Developer roles
* AI/ML internships
* NLP projects
* Data Analyst portfolios
* HR Automation projects

---

# 🧠 Key Features

✅ Dynamic Resume Upload
✅ PDF/DOCX/TXT Resume Parsing
✅ NLP Text Cleaning
✅ Semantic Resume Matching
✅ Sentence Transformer Embeddings
✅ AI-Based ATS Scoring
✅ Skill Extraction
✅ Missing Skill Detection
✅ Candidate Ranking
✅ Resume Shortlisting
✅ Interactive Streamlit Dashboard
✅ Analytics Charts
✅ CSV Report Download
✅ Recruiter Threshold Controls

---

# 🏗️ System Workflow

```text
Resume Upload
      ↓
Resume Parsing
      ↓
Text Cleaning
      ↓
Skill Extraction
      ↓
Sentence Transformer Embeddings
      ↓
Semantic Similarity Matching
      ↓
ATS Score Calculation
      ↓
Missing Skill Analysis
      ↓
Candidate Ranking
      ↓
Shortlist / Reject Decision
      ↓
Analytics Dashboard & CSV Export
```

---

# 🛠️ Tech Stack

## Programming Language

* Python

## Libraries & Frameworks

* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Sentence Transformers
* PyPDF2
* pdfplumber
* python-docx
* Plotly
* NLTK

## AI / NLP Concepts

* Natural Language Processing (NLP)
* Semantic Similarity
* Sentence Embeddings
* Cosine Similarity
* Skill Extraction
* Resume Parsing

---

# 📂 Project Structure

```text
Automated-Resume-Screening-Tool/
│
├── data/
│   ├── job_description.txt
│   ├── required_skills.txt
│
├── outputs/
│
├── src/
│   ├── __init__.py
│   ├── extractor.py
│   ├── cleaner.py
│   ├── matcher.py
│   ├── scorer.py
│   ├── advanced_matcher.py
│   └── report_generator.py
│
├── images/
│
├── docs/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/shwetasingh199/Automated-Resume-Screening-Tool
```

## 2️⃣ Open Project Folder

```bash
cd Automated-Resume-Screening-Tool
```

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The Streamlit dashboard will automatically open in your browser.

---

# 📤 How to Use

1. Upload resumes in:

   * PDF
   * DOCX
   * TXT format

2. Edit or provide the Job Description.

3. The system will:

   * Extract resume text
   * Analyze skills
   * Calculate ATS score
   * Detect missing skills
   * Rank candidates automatically

4. Download screening report as CSV.

---

# 📊 ATS Scoring Logic

The system uses:

* Sentence Transformer Embeddings
* Semantic Similarity
* Skill Matching
* Missing Skill Detection

### ATS Decisions

| ATS Score | Decision           |
| --------- | ------------------ |
| 80+       | Highly Recommended |
| 60–79     | Shortlisted        |
| 40–59     | Consider           |
| Below 40  | Rejected           |

---

# 📈 Dashboard Features

* Resume Ranking Table
* ATS Score Visualization
* Candidate Distribution Pie Chart
* Skill Match Analysis
* Recruiter Threshold Controls
* CSV Export

---

# 📸 Screenshots

## Dashboard
## When resume is above ATS score:

![Uploading Screenshot 2026-05-17 004339.png…]()
<img width="1476" height="832" alt="Screenshot 2026-05-17 004443" src="https://github.com/user-attachments/assets/4a68f40c-1c31-4dc1-a655-3a23f604fe24" />
<img width="1478" height="742" alt="Screenshot 2026-05-17 004432" src="https://github.com/user-attachments/assets/e7d05f13-a10e-472d-aa41-33ccf63967ea" />
<img width="1523" height="713" alt="Screenshot 2026-05-17 004420" src="https://github.com/user-attachments/assets/3dda4155-9483-4984-8616-e327233e64b3" />
<img width="1501" height="812" alt="Screenshot 2026-05-17 004402" src="https://github.com/user-attachments/assets/41011a6b-ac32-407d-8173-1a7d02504d05" />

## When resume is less than ATS score:

<img width="1901" height="833" alt="Screenshot 2026-05-17 004604" src="https://github.com/user-attachments/assets/9580157d-88d1-4fd4-8b02-0808fd6ab935" />
<img width="1442" height="707" alt="Screenshot 2026-05-17 004551" src="https://github.com/user-attachments/assets/bf50c6ed-8f6b-4ca2-bad9-8f6a3eebd612" />
<img width="1517" height="608" alt="Screenshot 2026-05-17 004541" src="https://github.com/user-attachments/assets/6abc8ca6-765d-4787-92f8-f16502ce09ae" />
<img width="1908" height="652" alt="Screenshot 2026-05-17 004515" src="https://github.com/user-attachments/assets/2061f63a-84d7-4982-9f8a-5ce161a7ed9a" />

---

# 🧪 Sample Test Cases

## Strong Resume

Expected:

* High ATS Score
* Highly Recommended

## Average Resume

Expected:

* Medium Score
* Consider / Shortlisted

## Unrelated Resume

Expected:

* Low Score
* Rejected

---

# 🧩 Future Improvements

* FastAPI Backend
* SQLite/PostgreSQL Database
* Recruiter Authentication
* Resume Recommendation Engine
* OpenAI Integration
* LangChain Support
* Vector Database
* Cloud Deployment
* Docker Support
* LLM-Based Explanations

---

# 📚 Learning Outcomes

Through this project I learned:

* NLP Fundamentals
* Semantic Search
* Resume Parsing
* ATS System Design
* Streamlit Dashboard Development
* AI-based Similarity Matching
* Python Modular Development
* Data Processing Pipelines
* GitHub Project Management

---


# 👩‍💻 Author

Shweta Singh

B.Tech Electronics and Computer Engineering Student

---

# ⭐ If You Like This Project

Give this repository a star ⭐ on GitHub.
