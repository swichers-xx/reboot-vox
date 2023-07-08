from flask_restful import Resource
import app

class ServiceResource(Resource):
    def get(self, server_name, service_name):
        # Get the status of the service
        service_status = app.get_service_status(server_name, service_name)

        return {'service_status': service_status}

    def post(self, server_name, service_name):
        # Toggle the status of the service
        app.toggle_service_status(server_name, service_name)

        return {'message': f'Toggled status of service {service_name} on server {server_name}'}
