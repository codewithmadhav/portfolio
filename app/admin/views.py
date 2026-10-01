import re

from app.models import SiteSetting


def slugify(value):
    value = (value or "").lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")


def reading_time(text):
    words = len(re.findall(r"\b\w+\b", text or ""))
    return max(1, round(words / 200))


def get_setting(key, default=""):
    setting = SiteSetting.query.filter_by(key=key).first()
    return setting.value if setting else default


def set_setting(key, value):
    setting = SiteSetting.query.filter_by(key=key).first()
    if setting:
        setting.value = value
        return setting
    new_setting = SiteSetting(key=key, value=value)
    return new_setting
