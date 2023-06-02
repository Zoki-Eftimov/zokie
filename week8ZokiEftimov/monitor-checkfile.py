#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#6-1-2023

# Description: This script reads the data of the file hashes -mysql-database-cmdb table-files. This script then checks these hashes against newly calculated hashes of the files on disk.

# Versioning
# Zoki: initial version v.0.1

# Set up initial variables and imports
import sys
import hashlib
from datetime import datetime
import pymysql
import csv

# MySQL database configuration information
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'cmdb',
}

# Function to connect to the database
def connect_to_database():
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()
        return connection, cursor
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

# Function to fetch file hashes from the database
def fetch_file_hashes(cursor):
    try:
        select_query = "SELECT path, hash, timestamp FROM files"
        cursor.execute(select_query)
        return cursor.fetchall()
    except pymysql.Error as err:
        print(f"Error fetching file hashes from database: {err}")
        return None

# Function to calculate the MD5 hash of a file
def calculate_md5_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            md5_hash = hashlib.md5()
            while chunk := file.read(4096):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return None
    except Exception as e:
        print(f"Error calculating hash for file {file_path}: {e}")
        return None

# Function to compare file hashes and generate the CSV file
def compare_file_hashes(file_hashes):
    rows = []
    for file_path, db_hash, db_timestamp in file_hashes:
        current_hash = calculate_md5_hash(file_path)
        if current_hash is None:
            status = "Error calculating hash"
        elif current_hash == db_hash:
            status = "OK"
        else:
            status = "File changed"

        row = [file_path, db_hash, db_timestamp, current_hash, status]
        rows.append(row)
    return rows

# Function to write data to a CSV file
def write_to_csv(data, file_path):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["filepath", "dbhash", "db hash date", "current hash", "status"])
            writer.writerows(data)
        print(f"CSV file '{file_path}' created successfully.")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

# This function closes the database connection
def close_database_connection(cursor, conn):
    cursor.close()
    conn.close()

# Main routine that is called when the script is run
def main():
    # Connect to the MySQL server
    conn, cursor = connect_to_database()

    # Fetch file hashes from the database
    file_hashes = fetch_file_hashes(cursor)
    if file_hashes is None:
        close_database_connection(cursor, conn)
        sys.exit(1)

    # Compare file hashes and generate the CSV data
    csv_data = compare_file_hashes(file_hashes)

    # Write the data to the CSV file
    write_to_csv(csv_data, "filecheck.csv")

    # Close the database connection
    close_database_connection(cursor, conn)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
