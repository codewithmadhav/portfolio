from flask import Blueprint, render_template, request
from app.models import Project, Post, Photo, ContactMessage
from app import db
from app.services.utils import get_setting

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    featured_projects = Project.query.filter_by(featured=True).all()[:3]
    recent_posts = Post.query.filter_by(published=True).order_by(Post.created_at.desc()).limit(3).all()
    gallery_preview = Photo.query.order_by(Photo.created_at.desc()).limit(4).all()
    return render_template(
        "index.html",
        featured_projects=featured_projects,
        recent_posts=recent_posts,
        gallery_preview=gallery_preview,
        site_name=get_setting("site_name", "Madhav"),
        site_email=get_setting("site_email", "hello@example.com"),
        github_url=get_setting("github_url", "https://github.com")
    )


@main_bp.route("/projects")
def projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template("project_detail.html", project=projects[0] if projects else None, is_listing=True, projects=projects)


@main_bp.route("/projects/<slug>")
def project_detail(slug):
    project = Project.query.filter_by(slug=slug).first_or_404()
    return render_template("project_detail.html", project=project, is_listing=False)
