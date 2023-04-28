#!/usr/bin/python3

#Zoran Eftimov
#Prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#4-27-2023

# This script takes birthdate and number of days as command line arguments and prints out the date that person will reach the number of days specified

# Versioning
# Zoki 4 - 27 - 23: initial version v.01

# Set up initial variables and imports
import sys
import datetime

# Main routine that is called when script is run
def main():

# Read arguments from the command line
    birthdate = sys.argv[1]
    days = int(sys.argv[2])

# convert birthdate to datetime object
    birthdate_date = datetime.datetime.strptime(birthdate, '%m-%d-%Y')

# calculate target date
    target_date = birthdate_date + datetime.timedelta(days=days)

# Format target date as MM-DD-YYYY
    target_date = target_date.strftime('%m-%d-%Y')

# print out target date
    print('\x1b[0;31;40m' + target_date + '\x1b[0m')
if __name__ == "__main__":
        main()
