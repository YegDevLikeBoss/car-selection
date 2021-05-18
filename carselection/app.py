from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

def create_app():
    app = Flask(__name__)
    CORS(app)

    register_routes(app)

    return app

def register_routes(app):
    @app.route("/")
    def hello():
        return "ok", 200