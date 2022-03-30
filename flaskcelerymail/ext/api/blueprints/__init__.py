from flask import Blueprint

site = Blueprint("site", __name__)
apibp = Blueprint("apibp", __name__, url_prefix="/api")
