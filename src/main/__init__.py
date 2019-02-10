from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/api/v1')

from . import views