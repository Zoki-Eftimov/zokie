#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-22-2023

# Description: This script reads the dhcpd log file and produces csv files, one that has a listing of all mac/IP addresses that ack, and second csv file that has the two Mac addresses that are ack'ing much more often than others.

# Versioning
# Zoki: initial version v.02

# Set up initial variables and imports
import re
import csv
import sys
import os

STATS = {}

#This function is searching for DHCPACK in the log file.
def ack_check(entry):
    #returning 1 if ack code is present
    if "DHCPACK" in entry:
        return 1
    else:
        return 0

#This function processes the DHCP log file and exracts MAC addresses and IP addresses using regular expressions.
def process_dhcp_log(log_file):
    with open(log_file, 'r') as file:
        for line in file:
            ack = ack_check(line)
            key = extract_key(line)
            if key in STATS:
                STATS[key] += ack
            else:
                STATS[key] = ack

#This function extracts all of the data and stores it as extracted_key
def extract_key(entry):
    ip_address_match = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", entry)
    mac_address_match = re.search("((?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2})", entry)
    if ip_address_match and mac_address_match:
        ip_address = ip_address_match.group()
        mac_address = mac_address_match.group()
        extracted_key = mac_address + "," + ip_address
        return extracted_key
    else:
    # Handle the case where a match was not found
        return None

#This function writes the DHCP statistics from the stats to a CSV file.
def write_stats_to_csv(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Mac address', 'IP address', 'Total number of acks'])
        for key, count in STATS.items():
            try:
                mac_address, ip_address = key.split(',')
                writer.writerow([mac_address, ip_address, count])
            except Exception:
                continue
    #prints success message indicating the creation of the file.
    print(f'Successfully created {csv_file} with DHCP statistics.')

#This function writes the problem MAC addresses to a text file.
def write_problem_macs(txt_file):
    #Sort problem MAC addresses by the number of acks in descending order
    sorted_macs = sorted(STATS.items(), key=lambda x: x[1], reverse=True)
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
    process_dhcp_log(log_file)
    # Write stats to CSV file
    write_stats_to_csv(csv_file)
    # Write problem MAC addresses to text file
    write_problem_macs(txt_file)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
