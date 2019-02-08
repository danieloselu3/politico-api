from flask import Flask
from config import config
from app.main import main


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    app.register_blueprint(main)

    
    return app