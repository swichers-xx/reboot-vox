from flask_restful import Resource
from app.models import ExampleModel

class ExampleResource(Resource):
    def get(self):
        return {'message': 'GET request to ExampleResource'}

    def post(self):
        return {'message': 'POST request to ExampleResource'}
