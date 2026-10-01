from flask import Blueprint, render_template, request

from app.models import Photo

gallery_bp = Blueprint("gallery", __name__)


@gallery_bp.route("/")
def gallery_index():
    album = request.args.get("album")
    photos = Photo.query.order_by(Photo.created_at.desc())
    if album:
        photos = photos.filter(Photo.album == album)
    photos = photos.all()
    albums = ["Urban", "Nature", "Travel", "Editorial", "Architecture"]
    return render_template("gallery/index.html", photos=photos, albums=albums, selected_album=album)
