# Freelance Personal Website (Flask)

Small personal portfolio website with:
- About section
- Services section
- Contact form
- Form messages stored in SQLite
- Optional email notification when someone submits contact form

## Run locally

```powershell
cd C:\projects\freelance-portfolio
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python app.py
```

Open: `http://127.0.0.1:5000/zenith-developing-full-stack-developer`

## Pages

- `/zenith-developing-full-stack-developer` (Home)
- `/zenith-developing-full-stack-developer/about`
- `/zenith-developing-full-stack-developer/services`
- `/zenith-developing-full-stack-developer/contact`

## Contact messages database

Messages are saved in `messages.db` in the project folder.

## Enable email notifications

Edit `.env` with your SMTP details:
- `MAIL_SERVER`
- `MAIL_PORT`
- `MAIL_USERNAME`
- `MAIL_PASSWORD`
- `CONTACT_RECEIVER`

For Gmail, use an App Password (not your account password).
"# freelancing-website" 
