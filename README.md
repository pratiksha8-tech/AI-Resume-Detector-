# 🤖 AI Resume Detector

An AI-powered Python web application that analyzes resumes and compares them with job descriptions using **Natural Language Processing (NLP)**, **TF-IDF**, and **Cosine Similarity**.

The system helps identify relevant skills, calculate a resume-job match percentage, find missing skills, preview extracted resume text, and generate a downloadable PDF analysis report.

---

## 📌 Project Overview

The **AI Resume Detector** is designed to automate basic resume screening and job matching.

Users can upload a resume in PDF format and enter a job description. The system extracts the resume text, detects skills from both the resume and job description, calculates text similarity, compares skills, and generates an overall match score.

The application provides a professional web interface using **Gradio**.

---

## ✨ Features

* 📄 Upload resume in PDF format
* 💼 Enter job description
* 🤖 AI/NLP-based resume analysis
* 🔍 Automatic skill detection
* 📊 Resume-job match percentage
* 🧠 TF-IDF text similarity
* 🔗 Cosine similarity
* ✅ Matched skills detection
* ❌ Missing skills detection
* 📃 Resume text preview
* 📈 Skill matching results
* 📥 Downloadable PDF analysis report
* 🌐 Professional Gradio web interface
* 🐍 Python-based implementation

---

## 🛠️ Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Main programming language |
| Gradio            | Web interface             |
| PyPDF             | PDF text extraction       |
| Scikit-learn      | Machine learning and NLP  |
| TF-IDF            | Text feature extraction   |
| Cosine Similarity | Resume-job similarity     |
| ReportLab         | PDF report generation     |
| HTML/CSS          | Dashboard styling         |

---

## 📂 Project Structure

```text
AI-Resume-Detector/
│
├── app.py
├── resume_detector.py
├── report_generator.py
├── skills.py
├── requirements.txt
├── README.md
│
└── sample/
    ├── sample_resume.pdf
    └── job_description.txt
```

### File Description

**`app.py`**
Main application file containing the Gradio web interface.

**`resume_detector.py`**
Contains PDF extraction, skill detection, text similarity, and resume-job matching logic.

**`report_generator.py`**
Generates the downloadable PDF analysis report.

**`skills.py`**
Contains the list of technical and soft skills used by the detector.

**`requirements.txt`**
Contains the Python libraries required to run the project.

**`sample/`**
Contains sample resume and job description files for testing.

---

## ⚙️ How the System Works

```text
Resume PDF
    ↓
Extract Resume Text
    ↓
Detect Resume Skills
    ↓
Enter Job Description
    ↓
Detect Job Skills
    ↓
TF-IDF Text Analysis
    ↓
Cosine Similarity
    ↓
Compare Skills
    ↓
Calculate Match Percentage
    ↓
Display Results
    ↓
Generate PDF Report
```

---

## 📊 Match Score

The system uses two main components:

### 1. Text Similarity

TF-IDF is used to convert the resume and job description into numerical vectors.

Cosine Similarity is then used to calculate their textual similarity.

### 2. Skill Matching

The system identifies skills present in the job description and checks whether those skills are present in the resume.

The final score combines the text similarity and skill matching results.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/AI-Resume-Detector.git
```

Move into the project folder:

```bash
cd AI-Resume-Detector
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run:

```bash
python app.py
```

The Gradio application will provide a web link that can be opened in a browser.

---

## 🖥️ How to Use

### Step 1

Open the AI Resume Detector webpage.

### Step 2

Upload your resume in **PDF format**.

### Step 3

Paste the required **Job Description**.

### Step 4

Click:

```text
🔍 ANALYZE RESUME
```

### Step 5

View:

* Overall Match Score
* Text Similarity
* Skill Match
* Matched Skills
* Missing Skills
* Resume Text Preview

### Step 6

Download the generated:

```text
AI_Resume_Analysis_Report.pdf
```

---

## 📄 Example Results

The system can display results such as:

```text
Overall Match: 78.5%

Text Similarity: 72.4%

Skill Match: 84.6%

Matched Skills:
✓ Python
✓ SQL
✓ MySQL
✓ HTML
✓ CSS
✓ Machine Learning
✓ Git
✓ GitHub

Missing Skills:
✗ AWS
✗ React
✗ Power BI
```

---

## 📦 Requirements

The project requires:

```text
gradio
pypdf
scikit-learn
reportlab
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🎓 Academic Project

This project can be used as a **Python, Artificial Intelligence, Machine Learning, or NLP academic project**.

### Project Title

**AI Resume Detector Using Python and Natural Language Processing**

### Project Objectives

* Automate basic resume screening.
* Extract useful information from resumes.
* Compare resumes with job descriptions.
* Identify relevant and missing skills.
* Calculate a resume-job matching score.
* Generate an easy-to-understand analysis report.

---

## 🔮 Future Enhancements

Possible future improvements include:

* Database integration
* User login and registration
* Multiple resume comparison
* Advanced NLP models
* Resume ranking
* Candidate dashboard
* Job recommendation system
* Cloud deployment
* Admin dashboard
* Resume keyword optimization
* Support for DOCX resumes

---

## ⚠️ Limitations

The current system primarily relies on text similarity and a predefined skill database. Therefore, the match percentage should be treated as an automated screening indicator rather than a definitive assessment of a candidate's suitability.

---

## 👩‍💻 Author

**Pratiksha Chavan**

Computer Science Student

---

## 📜 License

This project is created for educational and academic purposes.
