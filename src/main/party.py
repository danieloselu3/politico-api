from flask import jsonify
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





