import re
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from skills import SKILLS


def extract_pdf_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def find_skills(text):

    text = text.lower()
    found = []

    for skill in SKILLS:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(set(found))


def calculate_similarity(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return similarity * 100


def analyze_resume(resume_file, job_description):

    resume_text = extract_pdf_text(resume_file)

    resume_skills = find_skills(resume_text)

    job_skills = find_skills(job_description)

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    text_score = calculate_similarity(
        resume_text,
        job_description
    )

    if job_skills:

        skill_score = (
            len(matched_skills) /
            len(job_skills)
        ) * 100

    else:

        skill_score = 0

    final_score = (
        text_score * 0.5 +
        skill_score * 0.5
    )

    return {
        "score": round(final_score, 2),
        "text_score": round(text_score, 2),
        "skill_score": round(skill_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_text": resume_text
    }
