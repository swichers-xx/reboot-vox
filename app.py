import subprocess

def get_service_status(server_name, service_name):
    # Run the command on the remote server and return the output
    return subprocess.check_output(["powershell", "-Command", f"Invoke-Command -ComputerName {server_name} -ScriptBlock {{ Get-Service -Name {service_name} }}"])

def get_service_list(server_name):
    # Run the command on the remote server and return the output
    return subprocess.check_output(["powershell", "-Command", f"Invoke-Command -ComputerName {server_name} -ScriptBlock {{ Get-Service }}"])
