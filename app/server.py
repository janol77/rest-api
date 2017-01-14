from app.db import db

import os
# Import flask and template operators
from flask import Flask


def create_app(config="config.ini"):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(__name__)
    if os.path.exists(config):
        app.config.from_pyfile(config)
    else:
        print("The app does not have a config.ini file")
    # Define the WSGI application object
    db.init_app(app)
    # Register blueprint(s)
    from api import task_bp as task
    app.register_blueprint(task, url_prefix='/api')
    from api import user_bp as user
    app.register_blueprint(user, url_prefix='/api')

    # Sample HTTP error handling
    # @app.errorhandler(404)
    # def not_found(error):
    #     return render_template('404.html'), 404

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host=app.config.get('HOST', '0.0.0.0'),
            port=app.config.get('PORT', 5000),
            debug=app.config.get('DEBUG', False)
            )
