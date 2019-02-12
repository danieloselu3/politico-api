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
def create_offices():
    office = {
        'id':request.json['id'],
        'name':request.json['name'],
        'type':request.json['type']
    }

    offices.append(office)

    return jsonify(
        {
            'status': 201,
            'message':'office successfully created'
        }
    )

@bp.route('/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    office = [office for office in offices if office['id']==office_id]
    return jsonify(
        {
            'status':200,
            'office':office
        }
    )







