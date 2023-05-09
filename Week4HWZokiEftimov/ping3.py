#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-8-2023

# Description: This script imports pinglib and uses the arguments to display results and output them to a CSV file.

# Versioning
# Zoki: initial version v.01

# Set up initial variables and imports
import sys
import pinglib
import csv
import os

# Main function that calls other functions defined
# This function is the entry point and calls the rest of the functions, and at the end writes to CSV file.
def main():
    targets = get_ping_targets()
    results = ping_hosts(targets)
    display_results(results)

    if len(sys.argv) == 3 and results:
        filename = sys.argv[2]
        write_to_csv(results, filename)

# This function retrieves the target to be pinged, either from a file or directly from the command line - then returns a list of targets
def get_ping_targets():
    if len(sys.argv) < 2:
        print("Usage: python ping3.py [filename | IP | DNS name] [csv output file]")
        return []

    targets = []
    target = sys.argv[1]

    if target.endswith('.txt') or target.endswith('.csv'):
        with open(target, 'r') as f:
            targets = [line.strip() for line in f.readlines()]
    else:
        targets.append(target)

    return targets
# This function pings each target in the list of targets using the ping this function from pinglib, then returns either the target and the ping time or the target and string "Not Found".
def ping_hosts(targets):
    results = []
    for target in targets:
        result = pinglib.pingthis(target)
        if result[0]:
            results.append((target, result[1]))
        else:
            results.append((target, 'Not found'))
    return results
# This function displays the results of the pings to the console.
def display_results(results):
    print('\x1b[31mIP, TimeToPing (ms)\x1b[0m')
    for result in results:
        if isinstance(result[1], float):
            print(f"{result[0]}, {result[1]}")
        else:
            print(f"{result[0]}, {result[1]}")
# This function writes the results of the pings to a CSV file - it takes the list of results and a filename as input, then writes the results to the file in CSV format.
def write_to_csv(results, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['IP', 'TimeToPing (ms)'])
        for result in results:
            writer.writerow([result[0], result[1]])

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
