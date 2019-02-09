from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app