from app import db

post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship("Post", back_populates="category")


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    posts = db.relationship("Post", secondary=post_tags, back_populates="posts")


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    featured_image = db.Column(db.String(300), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    published = db.Column(db.Boolean, default=True)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    category = db.relationship("Category", back_populates="posts")
    tags = db.relationship("Tag", secondary=post_tags, back_populates="tags")


class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    github_url = db.Column(db.String(300), nullable=True)
    live_url = db.Column(db.String(300), nullable=True)
    image_url = db.Column(db.String(300), nullable=False)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class Photo(db.Model):
    __tablename__ = "photo"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    caption = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(300), nullable=False)
    album = db.Column(db.String(100), default="General")
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class ContactMessage(db.Model):
    __tablename__ = "contact_message"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class SiteSetting(db.Model):
    __tablename__ = "site_setting"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
