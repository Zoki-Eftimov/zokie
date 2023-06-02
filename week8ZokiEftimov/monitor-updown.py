#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#6-1-2023

# Description: This script is pinging the external IPs of the linux and windows server, and monitoring their status, creating a CSV file called updown.csv that records the timestamp and the status of the server.

# Versioning
# Zoki: initial version v.0.1

# Set up initial variables and imports
import csv
import time
from datetime import datetime
import subprocess
import sys

#Main function that calls the rest of the functions and specifies files that will be used.
def main():
    # Get the filename and file format from the command line arguments
    filename = "servers.csv"
    file_format = "csv"

    # Read the server IPs from the specified file
    servers = read_servers(filename, file_format)

    # Write the header row to updown.csv
    write_header()

    for _ in range(4):
        # Get the current timestamp
        timestamp = datetime.now().isoformat()

        # Ping each server and write the results to updown.csv
        for server in servers:
            result = pingthis(server)
            write_result(timestamp, server, result)
        print("\033[91m***Server status updated:***\033[0m")
        print_current_csv()
        # Wait for 10 seconds before checking the servers again
        time.sleep(10)

def read_servers(filename, file_format):
    # Read the server IPs from the specified file and return a list
    servers = []
    with open(filename, 'r') as file:
        if file_format == 'csv':
            reader = csv.reader(file)
            for row in reader:
                servers.append(row[0])
        # Add support for other file formats here if needed
    return servers

def pingthis(ipordns):
    # Ping the given IP or DNS and return the result
    try:
        output = subprocess.check_output(['ping', '-c', '1', ipordns])
        time_to_ping = round(float(output.split(b'time=')[1].split(b' ')[0]))
        return 'up'
    except subprocess.CalledProcessError:
        return 'down'

#This is a function that just reads the current content of updown.csv and prints it out
def print_current_csv():
    with open('updown.csv', 'r') as file:
        content = file.read()
        print(content)

def write_header():
    # Write the header row to updown.csv
    with open('updown.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['\033[94mdate\033[0m', '\033[94mexternal ip\033[0m', '\033[94mstatus\033[0m'])
       #writer.writerow(['date', 'external ip', 'status'])

def write_result(timestamp, server, result):
    # Write the result to updown.csv
    with open('updown.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, server, result])

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
