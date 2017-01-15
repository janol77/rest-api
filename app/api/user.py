# Import flask dependencies
from flask import request, jsonify
from werkzeug import generate_password_hash
# Import module models (i.e. User)
from models.user import User
from tools.tools import not_found, bad_request

# Define the blueprint: 'auth', set its url prefix: url/auth
from . import user_bp as user
import json


# Set the route and accepted methods
@user.route('/user/', methods=['GET'])
@user.route('/user/<string:key>/', methods=['GET'])
def get(key=None):
    if key is None:
        query = User.objects.order_by('email')
        users = [v.serialize() for v in query.all()]
        return jsonify({'status': 'OK',
                        'result': users})
    else:
        user = User.objects.filter(id=key).first()
        if user:
            return jsonify({'status': 'OK',
                            'result': user.serialize()})
        else:
            return not_found("the user does not exist")


# Set the route and accepted methods
@user.route('/user/<string:key>/', methods=['PUT'])
def put(key):
    try:
        new_data = json.loads(request.data)
        keys = User._db_field_map.keys()
        keys.remove('id')
        update_dict = {}
        for k in keys:
            if k not in new_data:
                raise ValueError
            if k is not 'password':
                update_dict[k] = new_data[k]
            else:
                update_dict[k] = generate_password_hash(new_data[k])

        user = User.objects.filter(id=key).first()
        if user:
            user.update(**update_dict)
        else:
            return not_found("the user does not exist")

    except ValueError:
        return bad_request('error en valores'), 400
    except KeyError:
        return bad_request('Conflicto en llaves'), 409
    return jsonify({'status': 'OK'}), 200

# Set the route and accepted methods
@user.route('/user/', methods=['POST'])
def post():
    return jsonify({'status': 'OK',
                    'result': 'post method'})
    # product = Product.query.get(productId)
    # if product:
    #     return jsonify({'status': 'OK',
    #                     'result': product.serialize()})
    # else:
    #     return not_found("the product does not exist")

# Set the route and accepted methods
@user.route('/user/<string:key>/', methods=['DELETE'])
def delete(key):
    user = User.objects.filter(id=key).first()
    if user:
        user.delete()
        return jsonify({'status': 'OK'}), 200
    else:
        return not_found("the user does not exist")
