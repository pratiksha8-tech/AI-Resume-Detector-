from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def create_report(
    score,
    matched_skills,
    missing_skills
):

    filename = "AI_Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "AI RESUME DETECTOR",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            f"Resume Match Score: {score}%",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Matched Skills",
            styles["Heading2"]
        )
    )

    for skill in matched_skills:

        story.append(
            Paragraph(
                "✓ " + skill.title(),
                styles["Normal"]
            )
        )

    story.append(
        Spacer(1, 15)
    )

    story.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    for skill in missing_skills:

        story.append(
            Paragraph(
                "✗ " + skill.title(),
                styles["Normal"]
            )
        )

    doc.build(story)

    return filename
