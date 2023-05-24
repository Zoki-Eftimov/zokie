#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-24-2023

# Description - This script runs nmap brite scan against nsd.org and prints out the DNS names and IP's into a csv file.

# Versioning
# Zoki: initial version v0.1

# Set up initial variables and imports
import csv
import nmap3

# This function performs the dns brute scan on the target nsd.org using nmap3 module
def perform_dns_brute_scan(target):
    nmap = nmap3.Nmap()
    results = nmap.nmap_dns_brute_script(target)
    return results

# This function writes the results to a CSV file
def write_dns_results_to_csv(results, output_file):
    fieldnames = ['DNS Name', 'IP']
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            dns_name = result['hostname']
            ip = result['address']
            if ':' not in ip:  # Ignore IPv6 entries
                writer.writerow({'DNS Name': dns_name, 'IP': ip})
    print(f"Scan results saved to '{output_file}'.")

# Main routine that is called when script is run
def main():
    # Perform the Nmap DNS brute scan
    target = "nsd.org"
    scan_results = perform_dns_brute_scan(target)

    # Save the results to CSV file
    output_file = 'nmap3a.csv'
    write_dns_results_to_csv(scan_results, output_file)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
