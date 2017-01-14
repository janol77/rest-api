# Import flask dependencies
from flask import request, jsonify

# Import module models (i.e. User)
from .models.user import User
from tools.tools import not_found

# Define the blueprint: 'auth', set its url prefix: url/auth
from . import user_bp as user


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
@user.route('/user/<int:key>/', methods=['PUT'])
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
@user.route('/user/<int:key>/', methods=['DELETE'])
def delete():
    return jsonify({'status': 'OK',
                    'result': 'delete method'})
    # product = Product.query.get(productId)
    # if product:
    #     return jsonify({'status': 'OK',
    #                     'result': product.serialize()})
    # else:
    #     return not_found("the product does not exist")