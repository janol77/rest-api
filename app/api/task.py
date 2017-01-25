"""Task.py."""
# Import flask dependencies
from flask import request, jsonify
# Import module models (i.e. User)
from models.task import Task
from tools.tools import not_found, bad_request

# Define the blueprint: 'auth', set its url prefix: url/auth
from . import task_bp as task
import json


# Set the route and accepted methods
@task.route('/task/', methods=['GET'])
@task.route('/task/<string:key>/', methods=['GET'])
def get(key=None):
    """Get Method."""
    if key is None:
        query = Task.objects.order_by('title')
        tasks = [v.serialize() for v in query.all()]
        return jsonify({'status': 'OK',
                        'result': tasks})
    else:
        task = Task.objects.filter(id=key).first()
        if task:
            return jsonify({'status': 'OK',
                            'result': task.serialize()})
        else:
            return not_found("Resource not found"), 404


# Set the route and accepted methods
@task.route('/task/<string:key>/', methods=['PUT'])
def put(key):
    """Put Method."""
    try:
        new_data = json.loads(request.data)
        keys = Task._db_field_map.keys()
        keys.remove('id')
        update_dict = {}
        for k in keys:
            if k not in new_data:
                raise ValueError
            update_dict[k] = new_data[k]

        task = Task.objects.filter(id=key).first()
        if task:
            task.update(**update_dict)
        else:
            return not_found("Resource not found"), 404

    except ValueError:
        return bad_request('Malformed post document'), 400
    except KeyError:
        return bad_request('Malformed post document'), 409
    return jsonify({'status': 'OK'}), 200


# Set the route and accepted methods
@task.route('/task/<string:key>/', methods=['PATCH'])
def patch(key):
    """Patch Method."""
    try:
        task = Task.objects.filter(id=key).first()
        if task:
            new_data = json.loads(request.data)
            keys = Task._db_field_map.keys()
            keys.remove('id')
            update_dict = {}
            for k in keys:
                if k in new_data:
                    update_dict[k] = new_data[k]
                    continue
            task.update(**update_dict)
        else:
            return not_found("Resource not found"), 404
    except ValueError:
        return bad_request('Malformed patch documen'), 400
    except KeyError:
        return bad_request('Unsupported patch document'), 415
    return jsonify({'status': 'OK'}), 200


# Set the route and accepted methods
@task.route('/task/', methods=['POST'])
def post():
    """Post Method."""
    try:
        new_data = json.loads(request.data)
        keys = Task._db_field_map.keys()
        keys.remove('id')
        update_dict = {}
        for k in keys:
            if k not in new_data:
                raise ValueError
            update_dict[k] = new_data[k]
        t = Task(**update_dict).save()
    except ValueError:
        return bad_request('Malformed post document'), 400
    except KeyError:
        return bad_request('Malformed post document'), 409
    return jsonify({'status': 'OK',
                    'result': t.serialize()}), 201


# Set the route and accepted methods
@task.route('/task/<string:key>/', methods=['DELETE'])
def delete(key):
    """Delete Method."""
    task = Task.objects.filter(id=key).first()
    if task:
        task.delete()
        return jsonify({'status': 'OK'}), 200
    else:
        return not_found("Resource not found"), 404
