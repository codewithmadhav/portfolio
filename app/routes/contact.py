from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Post, Category, Tag
from app.services.utils import reading_time, get_setting

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def blog_index():
    query = request.args.get("q", "")
    category_slug = request.args.get("category")
    tag_slug = request.args.get("tag")

    posts = Post.query.filter_by(published=True)
    if query:
        posts = posts.filter(Post.title.ilike(f"%{query}%") | Post.summary.ilike(f"%{query}%"))
    if category_slug:
        posts = posts.join(Post.category).filter(Category.slug == category_slug)
    if tag_slug:
        posts = posts.join(Post.tags).filter(Tag.slug == tag_slug)

    posts = posts.order_by(Post.created_at.desc()).all()
    featured_posts = Post.query.filter_by(published=True, featured=True).limit(3).all()
    categories = Category.query.order_by(Category.name).all()
    tags = Tag.query.order_by(Tag.name).all()
    return render_template(
        "blog/list.html",
        posts=posts,
        featured_posts=featured_posts,
        categories=categories,
        tags=tags,
        site_name=get_setting("site_name", "Madhav"),
        search_query=query,
    )


@blog_bp.route("/<slug>")
def blog_detail(slug):
    post = Post.query.filter_by(slug=slug, published=True).first_or_404()
    categories = Category.query.order_by(Category.name).all()
    related_posts = Post.query.filter(Post.id != post.id, Post.published.is_(True), Post.category_id == post.category_id).order_by(Post.created_at.desc()).limit(3).all()
    reading_time_minutes = reading_time(post.content)
    return render_template(
        "blog/detail.html",
        post=post,
        categories=categories,
        related_posts=related_posts,
        reading_time=reading_time_minutes,
    )
