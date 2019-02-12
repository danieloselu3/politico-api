from flask import jsonify
from . import bp


@bp.route('/')
def index():
    return jsonify({
        'status':'200',
        'note':'Welcome to politico'
    })




