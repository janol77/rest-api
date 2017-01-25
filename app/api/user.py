"""Summary."""
# Import flask dependencies
from flask import request, jsonify
from bson.dbref import DBRef
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
    """Get Method."""
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
            return not_found("Resource not found"), 404


# Set the route and accepted methods
@user.route('/user/<string:key>/', methods=['PUT'])
def put(key):
    """Put Method."""
    try:
        new_data = json.loads(request.data)
        keys = User._db_field_map.keys()
        keys.remove('id')
        update_dict = {}
        for k in keys:
            if k not in new_data:
                raise ValueError
            if k is 'password':
                update_dict[k] = generate_password_hash(new_data[k])
                continue
            if k is 'tasks':
                tasks = [DBRef('Task', task['id']) for task in new_data[k]]
                update_dict[k] = tasks
                continue
            update_dict[k] = new_data[k]
        user = User.objects.filter(id=key).first()
        if user:
            user.update(**update_dict)
        else:
            return not_found("Resource not found"), 404

    except ValueError:
        return bad_request('Malformed post document'), 400
    except KeyError:
        return bad_request('Malformed post document'), 400
    return jsonify({'status': 'OK'}), 200


# Set the route and accepted methods
@user.route('/user/<string:key>/', methods=['PATCH'])
def patch(key):
    """Patch Method."""
    try:
        user = User.objects.filter(id=key).first()
        if user:
            new_data = json.loads(request.data)
            keys = User._db_field_map.keys()
            keys.remove('id')
            update_dict = {}
            for k in keys:
                if k not in new_data:
                    continue
                if k is 'password':
                    update_dict[k] = generate_password_hash(new_data[k])
                    continue
                if k is 'tasks':
                    tasks = [DBRef('Task', task['id']) for task in new_data[k]]
                    update_dict[k] = tasks
                    continue
                update_dict[k] = new_data[k]

            user.update(**update_dict)
        else:
            return not_found("Resource not found"), 404
    except ValueError:
        return bad_request('Malformed patch documen'), 400
    except KeyError:
        return bad_request('Unsupported patch document'), 400
    return jsonify({'status': 'OK'}), 200


# Set the route and accepted methods
@user.route('/user/', methods=['POST'])
def post():
    """Post Method."""
    try:
        new_data = json.loads(request.data)
        keys = User._db_field_map.keys()
        keys.remove('id')
        update_dict = {}
        for k in keys:
            if k not in new_data:
                raise ValueError
            if k is 'password':
                update_dict[k] = generate_password_hash(new_data[k])
                continue
            if k is 'tasks':
                update_dict[k] = [task['id'] for task in new_data[k]]
                continue
            update_dict[k] = new_data[k]
        u = User(**update_dict).save()
    except ValueError:
        return bad_request('Malformed post document'), 400
    except KeyError:
        return bad_request('Malformed post document'), 409
    return jsonify({'status': 'OK',
                    'result': u.serialize()}), 201


# Set the route and accepted methods
@user.route('/user/<string:key>/', methods=['DELETE'])
def delete(key):
    """Delete Method."""
    user = User.objects.filter(id=key).first()
    if user:
        user.delete()
        return jsonify({'status': 'OK'}), 200
    else:
        return not_found("Resource not found"), 404
