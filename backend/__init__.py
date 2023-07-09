# import stuff
from flask import Flask

# from flask_sqlalchemy import SQLAlchemy
# from flask_redis import FlaskRedis

# Globally accessible libraries
# database = SQLAlchemy()
# redis = FlaskRedis()


# Create flask app
def create_app():
    app = Flask(__name__)

    # derive configuration values
    app.config.from_object("config.DevelopmentConfig")

    register_blueprints(app)
    initialize_extensions(app)
    configure_logging(app)
    register_error_handlers(app)

    # Initialize Plugins (the global ones)
    # database.init_app(app)
    # redis.init_app(app)

    # define context
    with app.app_context():
        # Include our Routes

        return app


def register_blueprints(app):
    from . import routes as routes_blueprint
    from . import api as api_blueprint

    # Register Blueprints
    app.register_blueprint(api_blueprint.api_bp, url_prefix="/api")
    app.register_blueprint(routes_blueprint.routes_bp)
    # app.register_blueprint(auth.auth_bp)
    # app.register_blueprint(admin.admin_bp)


def initialize_extensions(app):
    # mail.init_app(app)
    pass


def register_error_handlers(app):
    pass


def configure_logging(app):
    pass
