#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-7-2023

# Description

# Versioning
# Zoki: initial version v0.1

# Set up initial variables and imports
import sys
import os
import pinglib

# Main routine that is called when script is run
def main():
    # Check for input argument when running the script
    if len(sys.argv) != 2:
        print("Usage: python ping2.py filename_or_IP_or_DNS_name")
        return

    input_arg = sys.argv[1]

    # Check if the input is a file
    if os.path.isfile(input_arg):
        # Open file and read lines
        with open(input_arg) as f:
            lines = f.readlines()

        # Print header line
        print('\x1b[31mIP, TimeToPing (ms)\x1b[0m')

        # Loop through lines and ping each IP or DNS name
        for line in lines:
            line = line.strip()  # remove newline character
            result = pinglib.pingthis(line)
            print(f"{result[0]}, {result[1]}")

    else:
        # Assume the input is a DNS name or IP
        result = pinglib.pingthis(input_arg)
        if result is None:
            print("Not found")
        else:
            print(f"{result[0]}, {result[1]}")

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
