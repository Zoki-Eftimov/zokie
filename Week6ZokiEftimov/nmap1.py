#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-20-2023

# Description - This script does a syn scan of 152.157.64.0/24 and 152.157.65.0/24 and creates a CSV file (nmap1.csv) of the IPs and open ports found.

# Versioning
# Zoki: initial version v.01
# Run this script with sudo privilleges

import nmap
import csv

# Define the IP ranges to scan
ip_ranges = ['152.157.64.0/24', '152.157.65.0/24']

# Create an Nmap scanner object
scanner = nmap.PortScanner()

# Perform the SYN scan for each IP range
scan_results = {}
for ip_range in ip_ranges:
    scan_result = scanner.scan(ip_range, arguments='-sS')
    scan_results.update(scan_result['scan'])

# Extract the open ports information
open_ports = {}
for ip, result in scan_results.items():
    open_ports[ip] = [str(port) for port in result['tcp'] if result['tcp'][port]['state'] == 'open']

# Write the results to a CSV file
output_file = 'nmap1.csv'
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = ['IP', 'Open Ports']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for ip, ports in open_ports.items():
        writer.writerow({'IP': ip, 'Open Ports': ' '.join(ports)})

print(f"Scan results saved to '{output_file}'.")

