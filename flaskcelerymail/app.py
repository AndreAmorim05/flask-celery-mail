from flask import Flask
from flask_cors import CORS

from flaskcelerymail.ext import config


def create_app():
    app = Flask(__name__)
    config.init_app(app)

    return app
