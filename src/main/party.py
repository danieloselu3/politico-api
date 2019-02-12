from flask import jsonify
from flask import request
from . import bp

parties = [
    {
        'id':1,
        'name':'ODM',
        'hqAddress':'Nairobi',
        'logoUrl':'odmparty'
    },
        {
        'id':2,
        'name':'PNU',
        'hqAddress':'Nairobi',
        'logoUrl':'pnuparty'
    },
        {
        'id':3,
        'name':'TNA',
        'hqAddress':'Nairobi',
        'logoUrl':'tnaparty'
    }
]

@bp.route('/parties', methods=['GET'])
def get_parties():
    return jsonify(
        {
            'status': 200,
            'parties':parties
        }
    )

@bp.route('/parties/', methods=['POST'])
def create_party():
    party = {
        'id':request.json['id'],
        'name':request.json['name'],
        'logoUrl':request.json['name'],
        'hqAddress':request.json['hqAddress']
    }
    parties.append(party)
    return jsonify({
        'status':201,
        'message':'party successfully created'
    })




