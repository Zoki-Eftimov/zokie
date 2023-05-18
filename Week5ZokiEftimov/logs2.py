#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-17-2023

# Description: This script reads the dhcpd log file and produces csv files, one that has a listing of all mac/IP addresses that ack, and second csv file that has the two Mac addresses that are ack'ing much more often than others.

# Versioning
# Zoki: initial version v.01

# Set up initial variables and imports
import re
import csv
import sys
import os

#This function processes the DHCP log file and exracts MAC addresses and IP addresses using regular expressions.
def process_dhcp_log(log_file):
    # Regular expression patterns
    mac_pattern = r'((?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2}))'
    ip_pattern = r'([0-9]{1,3}(?:\.[0-9]{1,3}){3})'

    # Dictionary to store the statistics
    stats = {}
    problem_macs = {}

    # Read the log file and process each line
    with open(log_file, 'r') as file:
        for line in file:
            # Extract MAC address and IP address using regex
            mac_match = re.search(mac_pattern, line)
            ip_match = re.search(ip_pattern, line)

            if mac_match and ip_match:
                mac_address = mac_match.group(0)
                ip_address = ip_match.group(0)

                # Increment the ack count for the MAC address
                key = f'{mac_address}-{ip_address}'
                if key in stats:
                    stats[key] += 1
                else:
                    stats[key] = 1

    # Identify problem MAC addresses
    for key, count in stats.items():
        mac_address = key.split('-')[0]
        if mac_address in problem_macs:
            problem_macs[mac_address] += count
        else:
            problem_macs[mac_address] = count
    return stats, problem_macs

#This function writes the DHCP statistics from the stats to a CSV file.
def write_stats_to_csv(stats, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Mac address', 'IP address', 'Total number of acks'])
        for key, count in stats.items():
            mac_address, ip_address = key.split('-')
            writer.writerow([mac_address, ip_address, count])
    #prints success message indicating the creation of the file.
    print(f'Successfully created {csv_file} with DHCP statistics.')

#This function writes the problem MAC addresses to a text file.
def write_problem_macs(problem_macs, txt_file):
    #Sort problem MAC addresses by the number of acks in descending order
    sorted_macs = sorted(problem_macs.items(), key=lambda x: x[1], reverse=True)
    with open(txt_file, 'w') as file:
        file.write('Problem MAC addresses:\n')
        #Write the top two MAC addresses with their ack count
        for mac_address, count in sorted_macs[:2]:
            file.write(f'{mac_address}: {count} acks\n')
    print(f'Successfully created {txt_file} with problem MAC addresses.')

#This is the main function that calls the other functions specified - coordinates the execution of the program.
def main():
    log_file = 'dhcpdsmall.log'
    csv_file = 'dhcp_stats.csv'
    txt_file = 'ProblemMacs.txt'

    # Check if the log file exists
    if not os.path.isfile(log_file):
        print(f'Error: Log file "{log_file}" not found.')
        sys.exit(1)

    # Process DHCP log and generate stats and problem MAC addresses
    stats, problem_macs = process_dhcp_log(log_file)

    # Write stats to CSV file
    write_stats_to_csv(stats, csv_file)

    # Write problem MAC addresses to text file
    write_problem_macs(problem_macs, txt_file)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
