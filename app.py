# Import the required module
import subprocess

# Define the server name
serverName = "Server01"

# Define the command to run
command = input("Enter the command to run: ")

# Run the command on the remote server
subprocess.run(["powershell", "-Command", f"Invoke-Command -ComputerName {serverName} -ScriptBlock {{ {command} }}"])
