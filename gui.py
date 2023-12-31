import tkinter as tk
from tkinter import messagebox
import app

# Create the main window
root = tk.Tk()

# Create a listbox for the servers
server_listbox = tk.Listbox(root)
server_listbox.pack()

# Create a listbox for the services
service_listbox = tk.Listbox(root)
service_listbox.pack()

# Function to update the service list when a server is selected
def update_service_list(event):
    # Get the selected server
    server = server_listbox.get(server_listbox.curselection())

    # Get the list of services on the server
    service_list = app.get_service_list(server)

    # Update the service listbox
    service_listbox.delete(0, tk.END)
    for service in service_list:
        service_listbox.insert(tk.END, service)

# Bind the function to the listbox
server_listbox.bind('<<ListboxSelect>>', update_service_list)

# Function to check the status of a service when it is selected
def check_service_status(event):
    # Get the selected server and service
    server = server_listbox.get(server_listbox.curselection())
    service = service_listbox.get(service_listbox.curselection())

    # Get the status of the service
    status = app.get_service_status(server, service)

    # Show a message box with the status
    messagebox.showinfo("Service Status", status)

# Bind the function to the listbox
service_listbox.bind('<<ListboxSelect>>', check_service_status)

# Function to update the status of important servers and services
def update_status_list():
    server_service_list = [('server1', 'service1'), ('server2', 'service2')]  # replace with actual list
    status_list = app.get_status_for_list(server_service_list)
    for server_name, service_name, status in status_list:
        color = 'green' if status == 'online' else 'red'
        label = tk.Label(root, text=f'{server_name} - {service_name}: {status}', bg=color)
        label.pack()

# Call update_status_list
update_status_list()

# Start the main loop
root.mainloop()
