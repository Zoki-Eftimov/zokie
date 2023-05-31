#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-31-2023

# Description: This script connects to the cmdb database and prints out the data in rows to csv and json format depending on user's preference.

# Versioning
# Zoki: initial version v.01

# Set up initial variables and imports
import sys
import csv
import json
import pymysql

# Database connection information
host = 'localhost'
user = 'root'
password = 'password'
database = 'cmdb'

#This function connects to the database with user's credentials and returns successful connection.
def connect_to_database():
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        #print("Connected to the database successfully!") For testing purposes
        return connection, cursor
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)
#This function retrieves the data from mysql database and prints message for success or error.
def retrieve_data(cursor):
    try:
        cursor.execute("SELECT * FROM device")
        rows = cursor.fetchall()
        #print("Data retrieved successfully!") For testing purpose.
        return rows
    except pymysql.Error as e:
        print(f"Error retrieving data from the table: {e}")
        sys.exit(1)
#This function writes to csv file the data.
def save_data_to_csv(rows):
    filename = 'database2.csv'
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'macaddress', 'ip', 'cpucount', 'disks', 'ram', 'ostype', 'osversion'])
            writer.writerows(rows)
        print(f"Data saved to {filename} in CSV format.")
    except IOError:
        print(f"Error saving data to {filename} in CSV format.")

#Function that retrieves data in json format
def save_data_to_json(rows):
    filename = 'database2.json'
    data = []
    for row in rows:
        data.append({
            'name': row[0],
            'macaddress': row[1],
            'ip': row[2],
            'cpucount': row[3],
            'disks': row[4],
            'ram': row[5],
            'ostype': row[6],
            'osversion': row[7]
        })
    try:
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"Data saved to {filename} in JSON format.")
    except IOError:
        print(f"Error saving data to {filename} in JSON format.")

#Main function that calls the rest of the functions
def main():
    # Connect to the database
    connection, cursor = connect_to_database()

    # Retrieve data from the 'device' table
    rows = retrieve_data(cursor)

    # Save data to CSV or JSON file
    output_format = sys.argv[1] if len(sys.argv) > 1 else None
#Here I specify that this format will return in either json or csv format, it works in both.
    if output_format == 'csv':
        save_data_to_csv(rows)
    elif output_format == 'json':
        save_data_to_json(rows)

    # Close the database connection
    connection.close()

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
