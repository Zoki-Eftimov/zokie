#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#6-1-2023

# Description: This script takes in a command line full file path and creates a MD5 hash of the file, adds the timestamp and the hash to database called files in the mysql server.

# Versioning
# Zoki: initial version v.0.1

# Set up initial variables and imports
import sys
import hashlib
from datetime import datetime
import pymysql

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
# This function calculates md5 hashes
def calculate_md5_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            md5_hash = hashlib.md5()
            while chunk := file.read(4096):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print("File not found.")
        return None
    except PermissionError:
        print("Permission denied.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
# This function inserts the data into the files table in the CMDB database.
def insert_file_data(cursor, conn, timestamp, file_path, file_hash):
    try:
        insert_query = "INSERT INTO files (timestamp, path, hash) VALUES (%s, %s, %s)"
        insert_values = (timestamp, file_path, file_hash)
        cursor.execute(insert_query, insert_values)
        conn.commit()
        print("Data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting data into 'files' table: {err}")

# This is a function that closes the database connection
def close_database_connection(cursor, conn):
    cursor.close()
    conn.close()

#Main routine that is called when script is run
def main():
    # Get the file path from command-line argument
    if len(sys.argv) < 2:
        print("Please provide a file path as a command-line argument.")
        sys.exit(1)
    file_path = sys.argv[1]

    # Connect to the MySQL server
    conn, cursor = connect_to_database()

    # Get the current timestamp in ISO format
    timestamp = datetime.utcnow().isoformat(timespec='milliseconds')

    # Calculate the MD5 hash of the file
    file_hash = calculate_md5_hash(file_path)
    if file_hash is None:
        close_database_connection(cursor, conn)
        sys.exit(1)

    # Insert the data into the 'files' table
    insert_file_data(cursor, conn, timestamp, file_path, file_hash)

    # Close the database connection
    close_database_connection(cursor, conn)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
