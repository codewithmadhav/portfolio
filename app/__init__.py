from flask import Flask, render_template, request, Response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from app.models import Category, Tag, Post, Project, Photo, ContactMessage, SiteSetting
import os

load_dotenv()

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    csrf.init_app(app)

    os.makedirs(os.path.join(app.root_path, "static", "uploads"), exist_ok=True)

    from app.routes.main import main_bp
    from app.routes.blog import blog_bp
    from app.routes.contact import contact_bp
    from app.routes.gallery import gallery_bp
    from app.admin.views import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp, url_prefix="/blog")
    app.register_blueprint(contact_bp)
    app.register_blueprint(gallery_bp, url_prefix="/gallery")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.route("/robots.txt")
    def robots():
        return Response(
            "User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n",
            mimetype="text/plain",
        )

    @app.route("/sitemap.xml")
    def sitemap():
        posts = Post.query.filter_by(published=True).all()
        projects = Project.query.filter_by(featured=True).all()
        urls = ["https://example.com/", "https://example.com/projects", "https://example.com/blog", "https://example.com/gallery", "https://example.com/contact"]
        for post in posts:
            urls.append(f"https://example.com/blog/{post.slug}")
        for project in projects:
            urls.append(f"https://example.com/projects/{project.slug}")
        xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
        for url in urls:
            xml += f"  <url><loc>{url}</loc></url>\n"
        xml += "</urlset>\n"
        return Response(xml, mimetype="application/xml")

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(os.path.join(app.root_path, "static"), "favicon.svg")

    with app.app_context():
        db.create_all()
        seed_data()

    return app


def seed_data():
    if Project.query.first():
        return

    # Categories
    data_science = Category(name="Data Science", slug="data-science")
    ml = Category(name="Machine Learning", slug="machine-learning")
    ai = Category(name="Generative AI", slug="generative-ai")
    db.session.add_all([data_science, ml, ai])
    db.session.flush()

    # Tags
    python_tag = Tag(name="Python", slug="python")
    flask_tag = Tag(name="Flask", slug="flask")
    ml_tag = Tag(name="ML", slug="ml")
    llm_tag = Tag(name="LLM", slug="llm")
    db.session.add_all([python_tag, flask_tag, ml_tag, llm_tag])
    db.session.flush()

    # Projects
    project_1 = Project(
        title="AI Insight Dashboard",
        slug="ai-insight-dashboard",
        short_description="A production-ready analytics platform for model monitoring and forecasting.",
        description="A full-stack analytics dashboard for monitoring ML experiments, tracking feature drift, and displaying business KPIs in a clean interface.",
        github_url="https://github.com/codewithmadhav",
        live_url="https://example.com",
        image_url="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80",
        featured=True,
    )
    project_2 = Project(
        title="Generative AI Workflow Studio",
        slug="generative-ai-workflow-studio",
        short_description="A prompt orchestration and AI workflow toolkit for rapid experimentation.",
        description="Designed to help teams prototype LLM pipelines, compare prompt strategies, and manage structured outputs with reusable workflows.",
        github_url="https://github.com/codewithmadhav",
        live_url="https://example.com",
        image_url="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=80",
        featured=True,
    )
    project_3 = Project(
        title="Vision Model QA Lab",
        slug="vision-model-qa-lab",
        short_description="Evaluation utilities for medical and industrial vision models.",
        description="A tool to benchmark classification models, review edge cases, and visualize prediction confidence across multiple conditions.",
        github_url="https://github.com/codewithmadhav",
        live_url="https://example.com",
        image_url="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
        featured=False,
    )
    db.session.add_all([project_1, project_2, project_3])

    # Posts
    post_1 = Post(
        title="Building a Reliable ML Pipeline in Python",
        slug="building-a-reliable-ml-pipeline-in-python",
        summary="Practical guidance for shipping machine learning projects with clean data flow, reliable validation, and measurable iteration.",
        content="""# Building a Reliable ML Pipeline in Python

A high-performing model is only part of the story. A production-ready machine learning workflow needs reliable data processing, structured evaluation, and clear deployment logic.

## Start with clean data contracts
Use consistent schemas, validation steps, and reproducible preprocessing. This helps catch silent drift early.

## Evaluate with business-aware metrics
Accuracy alone is often misleading. Use metrics that reflect the real-world cost of false positives and false negatives.

## Protect the deployment layer
Build monitoring from the start so you can track confidence, latency, and data shifts after launch.

> Practical ML systems are operational systems first, and analytical experiments second.
""",
        featured_image="https://images.unsplash.com/photo-1526379095098-d400fd0bf935?auto=format&fit=crop&w=1200&q=80",
        category_id=data_science.id,
        published=True,
        featured=True,
    )
    post_1.tags.extend([python_tag, ml_tag])

    post_2 = Post(
        title="From Prompt Experimentation to GenAI System Design",
        slug="from-prompt-experimentation-to-genai-system-design",
        summary="A simple framework to move from playful prompt testing to robust AI workflows and production thinking.",
        content="""# From Prompt Experimentation to GenAI System Design

Rapid prototyping is exciting, but resilient AI systems require structure. Start with the business problem, then design around evaluation, observability, and feedback loops.

## Focus on workflow quality
Define inputs, outputs, failure cases, and escalation logic before scaling a prototype.

## Add evaluation checkpoints
Track quality with benchmark sets, human reviews, and prompt/version comparisons.

## Build for iteration
The best GenAI systems are easy to update as requirements evolve.
""",
        featured_image="https://images.unsplash.com/photo-1531746790731-6c087fecd65a?auto=format&fit=crop&w=1200&q=80",
        category_id=ai.id,
        published=True,
        featured=False,
    )
    post_2.tags.extend([flask_tag, llm_tag])

    db.session.add_all([post_1, post_2])

    # Gallery photos
    photos = [
        Photo(title="Night Horizon", caption="Early evening study in city light and atmosphere.", image_url="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80", album="Urban"),
        Photo(title="Quiet Structure", caption="Details shaped by contrast, form, and calm light.", image_url="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=1200&q=80", album="Nature"),
        Photo(title="Movement in Motion", caption="Documenting rhythm in a busy, layered environment.", image_url="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=80", album="Travel"),
        Photo(title="Editorial Light", caption="Minimal composition with texture and shadow.", image_url="https://images.unsplash.com/photo-1504593811423-6dd665756598?auto=format&fit=crop&w=1200&q=80", album="Editorial"),
        Photo(title="High Contrast", caption="A study in architecture, composition, and tone.", image_url="https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80", album="Architecture"),
        Photo(title="Warm Drift", caption="Soft color, slower movement, and reflective surfaces.", image_url="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80", album="Nature"),
    ]
    db.session.add_all(photos)

    settings = [
        SiteSetting(key="site_name", value="Madhav"),
        SiteSetting(key="site_email", value="hello@example.com"),
        SiteSetting(key="github_url", value="https://github.com/codewithmadhav"),
        SiteSetting(key="linkedin_url", value="https://www.linkedin.com"),
        SiteSetting(key="instagram_url", value="https://www.instagram.com"),
        SiteSetting(key="twitter_url", value="https://x.com"),
    ]
    db.session.add_all(settings)
    db.session.commit()

