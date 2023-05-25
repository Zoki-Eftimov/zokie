#!/usr/bin/python3
#!/usr/local/lib/python3.10
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-22-2023

# Description - This script reads the IP addresses from CSV file, then performs OS detection scan on these IP addresses. The data that gets stored is the most accurate OS detected data.

# Versioning
# Zoki: initial version v.0.1

# Set up initial variables and imports
import sys
import csv
import nmap3
import datetime

# Function that will read IP addresses from a CSV file, then returns IP addresses to main.
def read_ip_addresses(file_path):
    ip_addresses = []
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            ip_addresses.append(row['IP'])
    return ip_addresses
# This function performs the OS detection, runs the nmap scan and looks for the best guess out of the multiple OS listed.
def perform_os_detection(ip_addresses):
    nmap = nmap3.Nmap()
    os_results = {}
    for ip in ip_addresses:
        scan_result = nmap.nmap_os_detection(ip, args='-T5')
        if 'osmatch' in scan_result[ip]:
            os_classes = scan_result[ip]['osmatch']
            best_guess = max(os_classes, key=lambda x: float(x.get('accuracy', 0)))
            os_results[ip] = best_guess['name']
        else:
            os_results[ip] = 'Unknown'
    return os_results

# This function writes the results to CSV file.
def write_results(input_file, output_file, os_results):
    fieldnames = ['IP', 'Open Ports', 'OS']
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        with open(input_file, 'r') as input_csv:
            reader = csv.DictReader(input_csv)
            for row in reader:
                ip = row['IP']
                open_ports = row['Open Ports']
                os_versions = [os_results.get(ip, 'Unknown')]
                best_guess_os = max(os_versions, key=os_versions.count)
                writer.writerow({'IP': ip, 'Open Ports': open_ports, 'OS': best_guess_os})
    print(f"OS Scan results saved to '{output_file}'.")

# Main routine that is called when script is run
def main():
    # Define file paths
    input_file = 'nmap1.csv'
    output_file = 'nmap2.csv'
    # Read IP addresses from nmap1.csv
    ip_addresses = read_ip_addresses(input_file)
    # Perform OS detection scan for each IP
    os_results = perform_os_detection(ip_addresses)
    # Write the results to nmap2.csv
    write_results(input_file, output_file, os_results)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
