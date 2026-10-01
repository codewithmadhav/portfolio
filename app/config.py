import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, '..', 'app.db')}",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    SITE_NAME = os.getenv("SITE_NAME", "Madhav")
    SITE_DESCRIPTION = os.getenv(
        "SITE_DESCRIPTION",
        "Data Science & AI/ML Engineer student focused on Python, ML, DL, GenAI, and practical AI engineering.",
    )
    SITE_EMAIL = os.getenv("SITE_EMAIL", "hello@example.com")
    GITHUB_URL = os.getenv("GITHUB_URL", "https://github.com/codewithmadhav")
    LINKEDIN_URL = os.getenv("LINKEDIN_URL", "https://www.linkedin.com")
    INSTAGRAM_URL = os.getenv("INSTAGRAM_URL", "https://www.instagram.com")
    TWITTER_URL = os.getenv("TWITTER_URL", "https://x.com")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
    ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH")
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
