from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import db
from app.models import ContactMessage
import re

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact_form():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip()
        subject = (request.form.get("subject") or "").strip()
        message = (request.form.get("message") or "").strip()
        website = request.form.get("website", "")

        if website:
            flash("Your message could not be sent.", "error")
            return redirect(url_for("main.index", _anchor="contact"))

        if not all([name, email, subject, message]):
            flash("Please complete all required fields.", "error")
            return redirect(url_for("main.index", _anchor="contact"))

        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("main.index", _anchor="contact"))

        if len(message) < 20:
            flash("Your message is too short. Please add more detail.", "error")
            return redirect(url_for("main.index", _anchor="contact"))

        if message.count(" ") == 0:
            flash("Please write a meaningful message.", "error")
            return redirect(url_for("main.index", _anchor="contact"))

        contact = ContactMessage(name=name, email=email, subject=subject, message=message)
        db.session.add(contact)
        db.session.commit()
        flash("Thanks for reaching out. Your message has been received.", "success")
        return redirect(url_for("main.index", _anchor="contact"))

    return render_template("index.html")
