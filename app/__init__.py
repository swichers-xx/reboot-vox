from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    # Initialize the app
    app = Flask(__name__)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # Initialize the database with the app
    db.init_app(app)

    # Import the resources
    from .resources import ExampleResource

    # Initialize the API
    api = Api(app)

    # Add the resources to the API
    api.add_resource(ExampleResource, '/example')

    return app
