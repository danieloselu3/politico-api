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

@bp.route('/offices', methods=['POST'])
def get_offices():
    office = {
        'id':request.json['id'],
        'name':request.json['name'],
        'type':request.json['type']
    }

    offices.append(office)

    return jsonify(
        {
            'status': 200,
            'message':'office successfully created'
        }
    )







