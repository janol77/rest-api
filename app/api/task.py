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
            return not_found("the task does not exist")


# Set the route and accepted methods
@task.route('/task/<string:key>/', methods=['PUT'])
def put(key):
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
            return not_found("the task does not exist")

    except ValueError:
        return bad_request('error en valores'), 400
    except KeyError:
        return bad_request('Conflicto en llaves'), 409
    return jsonify({'status': 'OK'}), 200


# Set the route and accepted methods
@task.route('/task/<string:key>/', methods=['PATCH'])
def patch(key):
    return jsonify({'status': 'OK',
                    'result': 'patch method'})
    # product = Product.query.get(productId)
    # if product:
    #     return jsonify({'status': 'OK',
    #                     'result': product.serialize()})
    # else:
    #     return not_found("the product does not exist")

# Set the route and accepted methods
@task.route('/task/', methods=['POST'])
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
@task.route('/task/<string:key>/', methods=['DELETE'])
def delete(key):
    task = Task.objects.filter(id=key).first()
    if task:
        task.delete()
        return jsonify({'status': 'OK'}), 200
    else:
        return not_found("the task does not exist")
