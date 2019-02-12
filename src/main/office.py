from flask import jsonify, request

from . import bp

offices = [
    {
        'id':1,
        'type':'Federal',
        'name':'President'
    },
    {
        'id':2,
        'type':'Federal',
        'name':'MP'
    },
    {
        'id':3,
        'type':'County',
        'name':'Gorvenor'
    }
]

@bp.route('/offices', methods=['GET'])
def get_offices():
    return jsonify(
        {
            'offices':offices,
            'status': 200
        }
    )







