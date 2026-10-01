# Portfolio Website

A clean, premium personal portfolio for a Data Science & AI/ML Engineer built with Python, Flask, SQLAlchemy, and a responsive dark-first design.

## Features
- Modern homepage with sections for bio, skills, projects, journey, blog preview, photography, achievements, and contact
- Real Flask blog with posts, categories, tags, search, featured posts, and related content
- Photography gallery with responsive grid and lightbox viewer
- Admin dashboard for blog and gallery management
- Contact form with database storage, validation, and spam protection
- Dark/light mode, sticky nav, smooth scrolling, progress bar, and back-to-top button
- SEO metadata, sitemap, robots.txt, and favicon support

## Local setup

1. Create and activate a virtual environment.

Windows PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies.
```powershell
pip install -r requirements.txt
```

3. Create environment variables.
```powershell
Copy-Item .env.example .env
```

Update values in `.env` as needed.

4. Run the app.
```powershell
set FLASK_APP=app
set FLASK_ENV=development
flask run
```

Then open `http://127.0.0.1:5000`.

## Admin login
- Username: value from `ADMIN_USERNAME`
- Password: value from `ADMIN_PASSWORD` or `ADMIN_PASSWORD_HASH`

## Project structure
- `app/` — application package
- `app/static/` — CSS, JavaScript, images, uploads
- `app/templates/` — Jinja templates
- `app/models/` — SQLAlchemy models
- `app/routes/` — route blueprints
- `app/admin/` — admin portal

## Notes
- The application creates a SQLite database automatically on first run.
- Sample content is seeded when the database is empty.
- Uploaded photos are saved into `app/static/uploads/`.
