#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-7-2023

# Description - this is a script that takes an IP or DNS name and pings it. 

# Versioning
# Zoki: initial version v.01

# Set up initial variables and imports
import sys
import subprocess

# Main routine that is called when script is run
def main():
    # Get the IP or DNS name from the command line argument
    ipordns = sys.argv[1]

    # Call pingthis function to ping the IP or DNS
    result = pingthis(ipordns)

    # Display the result
    print(f"{result[0]}, {result[1]}")

def pingthis(ipordns):
    # Ping the given IP or DNS and return the result
    try:
        output = subprocess.check_output(['ping', '-c', '1', ipordns])
        time_to_ping = round(float(output.split(b'time=')[1].split(b' ')[0]))
        return [ipordns, time_to_ping]
    except subprocess.CalledProcessError:
        return [ipordns, 'Not Found']



# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
