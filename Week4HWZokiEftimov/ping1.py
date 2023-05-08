#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-7-2023

# Description - this script reads data from pingfile.txt and pings each one of the IP or DNS, outputs the time to ping  in ms.

# Versioning
# Zoki: initial version v.01

# Set up initial variables and imports (importing the pinglib)
import sys
import pinglib

# Main routine that is called when script is run
def main():
    # Check for filename argument when running the script
    if len(sys.argv) != 2:
        print("Usage: python ping1.py filename")
        return

    # Open file and read lines, reads all lines from the file and stores them in lines variable
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    # Print header line
    print('\x1b[31mIP, TimeToPing (ms)\x1b[0m')

    # Loop through lines and ping each IP or DNS name
    for line in lines:
        line = line.strip()  # remove newline character
        result = pinglib.pingthis(line)
        print(f"{result[0]}, {result[1]}")

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
