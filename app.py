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
        
def get_status_for_list(server_service_list):
    status_list = []
    for server_name, service_name in server_service_list:
        status = get_service_status(server_name, service_name)
        status_list.append((server_name, service_name, status))
    return status_list
