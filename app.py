import os
import smtplib
import sqlite3
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, Response, flash, redirect, render_template, request, send_file, url_for
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "messages.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-secret")
SITE_SLUG = "zenith-developing-full-stack-developer"
SITE_TITLE = "Zenith Developing || Full Stack Developer"
LINKEDIN_URL = "https://www.linkedin.com/in/atik-b-566254321/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BWMNJ1DSTSO%2BdNfSy3rP%2Fcw%3D%3D"
CONTACT_EMAIL = "atikbhas92@gmail.com"
CONTACT_PHONE = "+91 8200611492"
WHATSAPP_URL = "https://wa.me/918200611492"
GITHUB_URL = "https://github.com/Atikbhas"
SITE_URL = "https://zenithdeveloping.tech"


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS contact_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                service TEXT DEFAULT '',
                budget TEXT DEFAULT '',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        # Migrate table if new columns don't exist yet
        try:
            conn.execute("ALTER TABLE contact_messages ADD COLUMN service TEXT DEFAULT ''")
        except Exception:
            pass
        try:
            conn.execute("ALTER TABLE contact_messages ADD COLUMN budget TEXT DEFAULT ''")
        except Exception:
            pass


def save_message(name: str, email: str, message: str, service: str = "", budget: str = "") -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO contact_messages (name, email, message, service, budget) VALUES (?, ?, ?, ?, ?)",
            (name, email, message, service, budget),
        )


def send_email_notification(name: str, email: str, message: str, service: str = "", budget: str = "") -> None:
    mail_server = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    mail_port = int(os.getenv("MAIL_PORT", "587"))
    mail_username = os.getenv("MAIL_USERNAME")
    mail_password = os.getenv("MAIL_PASSWORD")
    receiver = os.getenv("CONTACT_RECEIVER", CONTACT_EMAIL)
    use_tls = os.getenv("MAIL_USE_TLS", "true").lower() == "true"

    if not (mail_server and mail_username and mail_password and receiver):
        return

    msg = EmailMessage()
    msg["Subject"] = f"New Client Inquiry: {name} ({service if service else 'General Project'})"
    msg["From"] = mail_username
    msg["To"] = receiver
    msg["Reply-To"] = email

    details = f"""You received a new client inquiry from your portfolio website!

==================================================
CLIENT INQUIRY DETAILS
==================================================
• Client Name        : {name}
• Client Email       : {email}
• Requested Service  : {service if service else 'Not Specified'}
• Estimated Budget   : {budget if budget else 'Not Specified'}

• Project Requirements & Message:
--------------------------------------------------
{message}
==================================================

You can reply directly to this email to contact {name} at {email}.
"""
    msg.set_content(details)

    with smtplib.SMTP(mail_server, mail_port, timeout=20) as server:
        if use_tls:
            server.starttls()
        server.login(mail_username, mail_password)
        server.send_message(msg)


init_db()


@app.context_processor
def inject_globals():
    return {
        "site_title": SITE_TITLE,
        "linkedin_url": LINKEDIN_URL,
        "github_url": GITHUB_URL,
        "site_slug": SITE_SLUG,
        "contact_email": CONTACT_EMAIL,
        "contact_phone": CONTACT_PHONE,
        "whatsapp_url": WHATSAPP_URL,
        "site_url": SITE_URL,
    }

@app.get("/robots.txt")
def robots_txt():
    content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    return Response(content, mimetype="text/plain")


@app.get("/sitemap.xml")
def sitemap_xml():
    urls = [
        f"{SITE_URL}/",
        f"{SITE_URL}/{SITE_SLUG}",
        f"{SITE_URL}/{SITE_SLUG}/services",
        f"{SITE_URL}/{SITE_SLUG}/projects",
        f"{SITE_URL}/{SITE_SLUG}/about",
        f"{SITE_URL}/{SITE_SLUG}/contact",
    ]
    xml_items = []
    for u in urls:
        xml_items.append(f"<url><loc>{u}</loc></url>")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join(xml_items)}
</urlset>"""
    return Response(xml, mimetype="application/xml")

@app.get("/")
def home():
    return redirect(url_for("home_page"))


@app.get(f"/{SITE_SLUG}/download-cv")
@app.get("/download-cv")
def download_cv():
    pdf_path = os.path.join(app.root_path, "static", "docs", "Atik_Bhas_Resume.pdf")
    if not os.path.exists(pdf_path):
        from generate_cv_pdf import create_resume_pdf
        create_resume_pdf(pdf_path)
    return send_file(
        pdf_path,
        as_attachment=True,
        download_name="Atik_Bhas_Resume.pdf",
        mimetype="application/pdf",
        conditional=False
    )


@app.get(f"/{SITE_SLUG}")
def home_page():
    return render_template("home.html")


@app.get(f"/{SITE_SLUG}/about")
def about_page():
    return render_template("about.html")


@app.get(f"/{SITE_SLUG}/services")
def services_page():
    return render_template("services.html")


@app.get(f"/{SITE_SLUG}/projects")
def projects_page():
    return render_template("projects.html")


@app.get(f"/{SITE_SLUG}/contact")
def contact_page():
    return render_template("contact.html")


@app.post(f"/{SITE_SLUG}/contact")
def contact_submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    service = request.form.get("service", "").strip()
    budget = request.form.get("budget", "").strip()

    if not name or not email or not message:
        flash("Please fill in all required fields (Name, Email, and Message).", "error")
        return redirect(url_for("contact_page"))

    save_message(name, email, message, service, budget)
    try:
        send_email_notification(name, email, message, service, budget)
    except Exception:
        flash("Your project request has been saved! (Email notification queued)", "warning")
        return redirect(url_for("contact_page"))

    flash("Thank you! Your project inquiry has been received. I will review it and reply within 24 hours.", "success")
    return redirect(url_for("contact_page"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
