# Windows Server Management API

This is a simple API for managing Windows servers and services.

## Installation

1. Ensure you have Python 3.6 or later installed. You can download Python from [here](https://www.python.org/downloads/).

2. Install the required Python packages. Navigate to the project directory in your terminal and run the following command:

```bash
pip install flask flask_restful flask_sqlalchemy
```

3. Clone the project from the Git repository. If you haven't already, you can clone the project using the following command (replace `your-repository-url` with the URL of your repository):

```bash
git clone your-repository-url
```

## Usage

1. Start the API server. In your terminal, navigate to the project directory and run the following command:

```bash
python run.py
```

This will start the API server on your local machine. You should see output indicating that the server is running, typically on `http://127.0.0.1:5000/`.

2. Use the API. You can now send requests to the API using a tool like [curl](https://curl.haxx.se/) or [Postman](https://www.postman.com/), or from your own code. Here are some example curl commands:

```bash
# Get the power status of a server
curl http://127.0.0.1:5000/server/Server01

# Toggle the power status of a server
curl -X POST http://127.0.0.1:5000/server/Server01

# Get the status of a service on a server
curl http://127.0.0.1:5000/service/Server01/wuauserv

# Toggle the status of a service on a server
curl -X POST http://127.0.0.1:5000/service/Server01/wuauserv
```

Replace `Server01` with the name of your server, and `wuauserv` with the name of the service you want to manage.

3. Use the GUI. You can also use the GUI to monitor servers and services. To start the GUI, run the following command in your terminal:

```bash
python gui.py
```

This will open a new window with a list of servers and services. Select a server to see its services, and select a service to see its status.

Please note that the actual functionality of the API and GUI will depend on how you've implemented the `get_power_status`, `toggle_power_status`, `get_service_status`, and `toggle_service_status` functions in the `app` module.
