from flask import Flask, abort, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

from .settings import Config
from .models import Makes, Cars
from .schemas import MakeSummary, Make, Car
from recommender.model import recommend

make_summary = MakeSummary()
make_schema = Make()
car_schema = Car()

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db = MongoEngine(app)
    register_routes(app)

    return app

def register_routes(app):
    @app.route("/", methods = ['GET'])
    def menu():
        makes = Makes.objects.all()
        return {"makes": [make_summary.dump(make) for make in makes]}, 200

    @app.route("/<make>", methods = ['GET'])
    def make(make):
        make = Makes.objects(name=make).first()
        if make == None:
            raise abort(404)
        return make_schema.dump(make), 200

    @app.route("/<make>/<model>", methods = ['GET'])
    def car(make, model):
        cars = Makes.objects(name=make).first()
        car = list(filter(lambda c: c.model==model, cars.models))[0]
        if car == None:
            abort(404)
        recommendation = recommend(str(car.id))
        car.recommended = [Cars.objects(id=car[0]).first() for car in recommendation]
        return car_schema.dump(car), 200