import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

def create_resume_pdf(output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Page setup with standard 0.5 in (36pt) margins
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    story = []
    
    # Color palette
    PRIMARY = colors.HexColor("#0f172a")     # Deep navy
    ACCENT = colors.HexColor("#0284c7")      # Vibrant cyan-blue
    TEXT_DARK = colors.HexColor("#1e293b")   # Body text
    TEXT_MUTED = colors.HexColor("#475569")  # Subtitle/labels
    BG_CARD = colors.HexColor("#f8fafc")     # Light card background
    BORDER_COLOR = colors.HexColor("#cbd5e1")# Clean divider
    
    # Typography styles
    styles = getSampleStyleSheet()
    
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=PRIMARY
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=ACCENT
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=TEXT_MUTED
    )
    
    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=PRIMARY,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_DARK
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_DARK,
        leftIndent=8
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=PRIMARY
    )
    
    job_meta_style = ParagraphStyle(
        'JobMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=ACCENT
    )
    
    tag_style = ParagraphStyle(
        'TagStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=ACCENT
    )

    # 1. Header Section: Name, Role, and Contact Information
    header_left = [
        Paragraph("ATIK BHAS", name_style),
        Spacer(1, 2),
        Paragraph("FULL STACK DEVELOPER &amp; BCA SOFTWARE ENGINEER", title_style),
        Spacer(1, 3),
        Paragraph("Specializing in Python/Flask, PHP, AI &amp; Machine Learning, SQL Architectures &amp; Modern Web Systems.", body_style)
    ]
    
    header_right = [
        Paragraph("<b>Location:</b> Rajkot, Gujarat, India", contact_style),
        Paragraph("<b>Email:</b> atikbhas92@gmail.com", contact_style),
        Paragraph("<b>Phone / WhatsApp:</b> +91 8200611492", contact_style),
        Paragraph("<b>LinkedIn:</b> linkedin.com/in/atik-b-566254321", contact_style),
        Paragraph("<b>GitHub:</b> github.com/Atikbhas", contact_style),
    ]
    
    header_table = Table([[header_left, header_right]], colWidths=[330, 210])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=6))

    # Helper function for section banners
    def add_section_header(title):
        story.append(Paragraph(title.upper(), section_heading_style))
        story.append(HRFlowable(width="100%", thickness=0.8, color=BORDER_COLOR, spaceAfter=5))

    # 2. Executive Professional Summary
    add_section_header("Professional Summary")
    summary_text = (
        "Versatile and results-driven <b>Full Stack Software Developer</b> and BCA student at <b>Saurashtra University</b> with proven expertise in building production-ready web applications, scalable backend systems with <b>Python/Flask</b> and <b>PHP</b>, intelligent <b>AI &amp; Machine Learning</b> workflows, and optimized <b>MySQL/SQLite</b> database architectures. Passionate about writing clean, maintainable code, implementing responsive modern interfaces, and solving real-world business challenges."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 6))

    # 3. Technical Skills Matrix (Two-Column Table)
    add_section_header("Technical Skills &amp; Core Competencies")
    skills_data = [
        [
            Paragraph("<b>Languages &amp; Web:</b>", tag_style),
            Paragraph("HTML5, Modern CSS3, JavaScript (ES6+), Bootstrap 5, Python 3, PHP 8, SQL", body_style)
        ],
        [
            Paragraph("<b>AI, ML &amp; Data Science:</b>", tag_style),
            Paragraph("Artificial Intelligence &amp; Machine Learning (AI/ML), Pandas, NumPy, Seaborn, Matplotlib, OpenCV / Computer Vision", body_style)
        ],
        [
            Paragraph("<b>Frameworks &amp; Backend:</b>", tag_style),
            Paragraph("Flask Framework, PHP MVC, RESTful APIs, Session Security, Authentication &amp; Role Management", body_style)
        ],
        [
            Paragraph("<b>Databases &amp; Storage:</b>", tag_style),
            Paragraph("MySQL, SQLite, Relational Schema Design, Query Optimization &amp; Performance Indexing", body_style)
        ],
        [
            Paragraph("<b>Developer Tools &amp; IDEs:</b>", tag_style),
            Paragraph("Git &amp; GitHub, Visual Studio Code, Jupyter Notebook, NetBeans IDE, cPanel / Render Cloud Hosting", body_style)
        ],
    ]
    skills_table = Table(skills_data, colWidths=[140, 400])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, -1), BG_CARD),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 6))

    # 4. Featured Projects & Engineering Experience
    add_section_header("Featured Projects &amp; Practical Experience")

    # Project 1: Smart AI Attendance System
    proj1_header = Table([
        [
            Paragraph("<b>Smart AI Attendance System</b> | <i>AI &amp; Computer Vision Web Application</i>", job_title_style),
            Paragraph("<b>Live on Render</b>", job_meta_style)
        ]
    ], colWidths=[400, 140])
    proj1_header.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(proj1_header)
    story.append(Paragraph("• Built an intelligent automated attendance platform utilizing computer vision &amp; facial recognition algorithms.", bullet_style))
    story.append(Paragraph("• Developed with Python and Flask backend, integrating facial landmark detection to mark student presences in &lt; 0.3s.", bullet_style))
    story.append(Paragraph("• Won College Hackathon distinction; deployed live on Render with automated analytics and instructor dashboards.", bullet_style))
    story.append(Spacer(1, 5))

    # Project 2: J.P. Imitation Jewellery Storefront
    proj2_header = Table([
        [
            Paragraph("<b>J.P. Imitation Jewellery Digital Storefront</b> | <i>Full Stack E-Commerce &amp; Admin</i>", job_title_style),
            Paragraph("<b>Client Project</b>", job_meta_style)
        ]
    ], colWidths=[400, 140])
    proj2_header.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(proj2_header)
    story.append(Paragraph("• Engineered a customized digital catalog and inventory management portal for a high-volume jewelry enterprise.", bullet_style))
    story.append(Paragraph("• Integrated 1-click WhatsApp checkout API, dynamic category filters, high-resolution product showcases, and admin control.", bullet_style))
    story.append(Paragraph("• Optimized SQL queries and frontend assets for lightning-fast mobile catalog browsing.", bullet_style))
    story.append(Spacer(1, 5))

    # Project 3: Zenith Developing / Freelance Web Engineering
    proj3_header = Table([
        [
            Paragraph("<b>Zenith Developing</b> | <i>Freelance Full Stack Engineering &amp; Solutions</i>", job_title_style),
            Paragraph("<b>2024 - Present</b>", job_meta_style)
        ]
    ], colWidths=[400, 140])
    proj3_header.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(proj3_header)
    story.append(Paragraph("• Deliver custom full-stack solutions, RESTful API integrations, and UI/UX modernization for diverse clients.", bullet_style))
    story.append(Paragraph("• Provide 100% code ownership, comprehensive documentation, secure authentication, and post-deployment support.", bullet_style))
    story.append(Spacer(1, 6))

    # 5. Education & Academic Qualifications
    add_section_header("Education &amp; Academic Qualifications")

    edu1_table = Table([
        [
            Paragraph("<b>Bachelor of Computer Applications (BCA)</b>", job_title_style),
            Paragraph("<b>Rajkot, Gujarat</b>", job_meta_style)
        ],
        [
            Paragraph("Saurashtra University | Coursework: Data Science, Machine Learning, Python, DBMS, DSA, Web Systems", body_style),
            Paragraph("Pursuing / Enrolled", job_meta_style)
        ]
    ], colWidths=[400, 140])
    edu1_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(edu1_table)
    story.append(Spacer(1, 4))

    edu2_table = Table([
        [
            Paragraph("<b>Higher Secondary Certificate (HSC / 12th)</b>", job_title_style),
            Paragraph("<b>Rajkot, Gujarat</b>", job_meta_style)
        ],
        [
            Paragraph("Masum Vidhyalay | Strong foundation in computing, statistics, mathematics, and logical reasoning", body_style),
            Paragraph("Completed", job_meta_style)
        ]
    ], colWidths=[400, 140])
    edu2_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(edu2_table)
    story.append(Spacer(1, 4))

    edu3_table = Table([
        [
            Paragraph("<b>Secondary School Certificate (SSC / 10th)</b>", job_title_style),
            Paragraph("<b>Rajkot, Gujarat</b>", job_meta_style)
        ],
        [
            Paragraph("Bhartiya School | Distinction in foundational sciences and analytical problem solving", body_style),
            Paragraph("Completed", job_meta_style)
        ]
    ], colWidths=[400, 140])
    edu3_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(edu3_table)
    story.append(Spacer(1, 6))

    # 6. Languages & Attributes
    add_section_header("Languages &amp; Professional Attributes")
    extra_data = [
        [
            Paragraph("<b>Spoken Languages:</b>", tag_style),
            Paragraph("English (Professional Working), Gujarati (Native), Hindi (Fluent)", body_style)
        ],
        [
            Paragraph("<b>Key Attributes:</b>", tag_style),
            Paragraph("Rapid Prototyping, Clean Architecture, Direct Communication, Agile Delivery, Problem Solving", body_style)
        ]
    ]
    extra_table = Table(extra_data, colWidths=[140, 400])
    extra_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(extra_table)

    # Build document
    doc.build(story)
    print(f"Successfully generated CV PDF at: {output_path}")

if __name__ == "__main__":
    output_pdf = os.path.join("static", "docs", "Atik_Bhas_Resume.pdf")
    create_resume_pdf(output_pdf)
