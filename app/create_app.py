# create_app.py

from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register blueprints (if you have any)
    # from .routes import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app
