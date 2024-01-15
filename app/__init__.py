from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

app = create_app()

from app.routes.root import *

if __name__ == '__main__':
    app.run()
