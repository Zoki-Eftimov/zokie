#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-14-2023

# Description: This script prints out the mac addresses of iphones and counts them. Then the result gets written to a file "iphone_macs.txt". 

# Versioning
# Zoki: initial version v.01

# Set up initial variables and imports
import sys
import re

#This function takes the name log file and attempts to open the file for reading (I set log file to be the dhcpdsmall file that I need to use for this script).
def open_log_file(log_file):
    try:
        with open(log_file, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        sys.exit(1)
#This function takes a list of the log file lines as input and processes each line to extract Iphone Mac addresses, it goes over each line that has the string "iPhone". Then the set of Iphone's mac addresses are returned.
def process_log_file(lines):
    iphone_macs = set()

    for line in lines:
        if 'iPhone' in line:
            match = re.search(r'(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})', line)
            if match:
                mac = match.group(1)
                iphone_macs.add(mac)
    return iphone_macs

#This function takes a set of MAC addresses and writes them to a file named iphone_macs.txt, it iterates over each MAC address; at the end writes the count of MAC addresses as a separate file.
def write_mac_addresses(mac_addresses):
    with open('iphone_macs.txt', 'w') as f:
        for mac in mac_addresses:
            f.write(mac + '\n')
        f.write(f"Count = {len(mac_addresses)}\n")
#Main function that imports the dhcpdsmall.log file, so the code can read lines from that file. then calls the other functions specified
def main():
    log_file = 'dhcpdsmall.log'

    lines = open_log_file(log_file)
    iphone_macs = process_log_file(lines)
    write_mac_addresses(iphone_macs)
    print("\033[91miPhone MAC addresses:\033[0m")
    for mac in iphone_macs:
        print(mac)
    print("Count =", len(iphone_macs))



# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
