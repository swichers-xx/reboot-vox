from flask_restful import Resource
import app

class ServerResource(Resource):
    def get(self, server_name):
        # Get the power status of the server
        power_status = app.get_power_status(server_name)

        return {'power_status': power_status}

    def post(self, server_name):
        # Toggle the power status of the server
        app.toggle_power_status(server_name)

        return {'message': f'Toggled power status of server {server_name}'}
