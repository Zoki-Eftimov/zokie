#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-24-2023

# Description - This script takes data from nmap3a.csv file, and then looks up the ip addresses using the ip-api.com API and returns data of this ip address and returns Geolocation information

# Versioning
# Zoki: initial version v.0.1

# Set up initial variables and imports
import csv
import requests

# Function to fetch geolocation information for an IP address
def get_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country = data.get("country", "")
        region = data.get("regionName", "")
        city = data.get("city", "")
        zipcode = data.get("zip", "")
        isp = data.get("isp", "")
        return country, region, city, zipcode, isp
    return "", "", "", "", ""

# Function to process the nmap3.csv file and generate nmap4.csv with geolocation information
def process_csv(input_file, output_file):
    fieldnames = ['DNS Name', 'IP', 'Country', 'RegionName', 'City', 'Zipcode', 'ISP']
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        with open(output_file, 'w', newline='') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                ip = row['IP']
                # Skip IPv6 addresses
                if ":" in ip:
                    continue
                dns = row['DNS Name']
                country, region, city, zipcode, isp = get_geolocation(ip)
                writer.writerow({'DNS Name': dns, 'IP': ip, 'Country': country, 'RegionName': region, 'City': city, 'Zipcode': zipcode, 'ISP': isp})
    print(f"\nGeolocation information saved to '{output_file}'.")

# Main function that calls the other functions
def main():
    input_file = 'nmap3a.csv'
    output_file = 'nmap4.csv'
    process_csv(input_file, output_file)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
