from flask import Blueprint

company_bp = Blueprint("company", __name__)
user_bp = Blueprint("user", __name__)

from app.blueprints import company
from app.blueprints import user
