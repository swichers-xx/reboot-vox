import subprocess
import logging

def get_service_status(server_name, service_name):
    try:
        # Run the command on the remote server and return the output
        return subprocess.check_output(["powershell", "-Command", f"Invoke-Command -ComputerName {server_name} -ScriptBlock {{ Get-Service -Name {service_name} }}"])
    except Exception as e:
        logging.error(f"Error getting service status: {e}")
        return "Error getting service status"

def get_service_list(server_name):
    try:
        # Run the command on the remote server and return the output
        return subprocess.check_output(["powershell", "-Command", f"Invoke-Command -ComputerName {server_name} -ScriptBlock {{ Get-Service }}"])
    except Exception as e:
        logging.error(f"Error getting service list: {e}")
        return "Error getting service list"
