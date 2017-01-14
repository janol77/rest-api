# Import flask dependencies
from flask import request, jsonify

# Import module models (i.e. User)
from tools.tools import not_found
from models.task import Task

# Define the blueprint: 'auth', set its url prefix: url/auth
from . import task_bp as task


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
@task.route('/task/<int:key>/', methods=['PUT'])
def put():
    return jsonify({'status': 'OK',
                    'result': 'put method'})
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
@task.route('/task/<int:key>/', methods=['DELETE'])
def delete():
    return jsonify({'status': 'OK',
                    'result': 'delete method'})
    # product = Product.query.get(productId)
    # if product:
    #     return jsonify({'status': 'OK',
    #                     'result': product.serialize()})
    # else:
    #     return not_found("the product does not exist")