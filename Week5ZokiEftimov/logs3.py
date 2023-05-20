#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-17-2023
####################
# Description: This script will search for an IP in the dhcpdsmall log file, get the mac address then lookup for this mac at api-macvendors.com to print out the vendor of the network device.
# Versioning
# Zoki: initial version v.01

# Set up initial variables and imports
import sys
import re
import csv
import time
import requests
# This function takes the name of the log file and attempts to open the file for reading.
def open_log_file(log_file):
    try:
        with open(log_file, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        sys.exit(1)
# This function is extracting the 4 target ip addreses and returns variable ip_addresses
def extract_ip_addresses():
    file_path = "target.txt"
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', contents)
            return ip_addresses
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

# This function processes the log file, finds the ip addresses that match and then matches them with mac address, then calls the vendor function.
def process_log_file(lines):
    ip_addresses = extract_ip_addresses()
    ip_mac_addresses = {}
    for line in lines:
        for ip in ip_addresses:
            ip_match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            mac_match = re.search(r'([0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5})', line)
            if ip_match and mac_match:
                ip_match_str = ip_match.group(1)
                mac_match_str = mac_match.group(1)
                if ip == ip_match_str:
                    vendor = get_mac_vendor(mac_match_str)
                    ip_mac_addresses[ip] = (mac_match_str, vendor)
    return ip_mac_addresses
#This function uses mac addresses to look up for their name with the api.mac.vendors.com (I am using sleep delay module to slow down and get all the results).
def get_mac_vendor(mac_match):
    url = f"https://api.macvendors.com/{mac_match}"
    delay = 1.25
    time.sleep(delay)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Error! Mac Address not found")
# This function is writing the data to a csv file dhcp_results.csv.
def write_csv_file(data, filename):
    print("==========================================================================================")
    print("\033[31mIP Address\tMAC Address\t\tVendor\033[0m")
    print("==========================================================================================")
    for ip, (mac, vendor) in data.items():
        print(f"{ip}\t{mac}\t{vendor}")
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Address', 'MAC Address', 'Vendor'])
        for ip, (mac, vendor) in data.items():
            writer.writerow([ip, mac, vendor])
# Main function that imports the dhcpdsmall.log file, processes the log file, performs a lookup of the MAC addresses, performs a lookup of the vendors and for the MAC addresses - then writes results to CSV file.
def main():
    log_file = 'dhcpdsmall.log'
    output_file = "dhcp_results.csv"
    target = 'target.txt'
    lines = open_log_file(log_file)
    ip_mac_addresses = process_log_file(lines)
    write_csv_file(ip_mac_addresses, output_file)
    print("\n\nOutput saved in dhcp_results.csv")
# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
