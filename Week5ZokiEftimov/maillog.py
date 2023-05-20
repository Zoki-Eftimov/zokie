#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-19-2023
###############################################
# Description: This script goes through the mail.log file and captures server names and their IP, prints out CSV file servers.csv and prints each server one time.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Versioning
# Zoki: initial version v.01
###############################################
# Set up initial variables and imports
import re
import csv

# This is function that searches the mail.log file for anything that has <> and .nsd.org, and then matches with IP address. The function returns the extracted server_name and IP address as a tuple.
def get_server_info(line):
    server_regex = r'<([^>]+)@?([^@>]+)?'
    server_regex_2 = r'(\S+\.nsd\.org)\b'
    ip_regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    server_match = re.search(server_regex, line)
    server_match_2 = re.search(server_regex_2, line)
    ip_match = re.search(ip_regex, line)
# if server match is successful the variable server_name is updated with the matched server_name from the group
    server_name = None
    if server_match:
        server_name = server_match.group(1) or server_match.group(2)
    if server_match_2:
        server_name = server_match_2.group()
# if IP address is successful it means that there is a match with ip_regex pattern, then the ip address is updated with the captured IP add from IP_match_group.
    ip_address = None
    if ip_match:
        ip_address = ip_match.group(1)
    return server_name, ip_address
# This is a function that writes to a CSV file named servers.csv
def write_to_csv(server_list, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['\033[34mServer Name\033[0m', '\033[34mServer IP\033[0m'])
        #set to store unique server names
        unique_servers = set()
        for server, ip in server_list:
            if server not in unique_servers:
                ip_address = ip.strip("[]")
                writer.writerow([server, ip])
                unique_servers.add(server)

## Main function that imports the mail.log file, searches for unique server and server ip, then prints out to csv file called servers.csv
def main():
    log_file = 'mail.log'
    output_file = 'servers.csv'
    server_list = []
    with open(log_file, 'r') as file:
        for line in file:
            server_name, ip_address = get_server_info(line)
            if server_name and ip_address:
                server_list.append((server_name, ip_address))
    if server_list:
        write_to_csv(server_list, output_file)
        with open(output_file, 'r') as csvfile:
            content = csvfile.read()
            lines = content.split('\n')
            print("******************************************************")
            print("\033[31mServers.csv file content:\033[0m")
            print("******************************************************")
            for line in lines:
                print(line.replace(',', '\t\t\t'))
        print("\nServers.csv has been generated.")
    else:
        print("Content not found!")


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
