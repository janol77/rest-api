from flask import Blueprint


user_bp = Blueprint('user', __name__)
task_bp = Blueprint('task', __name__)

from . import task, user

@task_bp.errorhandler(404)
@user_bp.errorhandler(404)
def not_found_handler(e):
    return not_found('resource not found')
