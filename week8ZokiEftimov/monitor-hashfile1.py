#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#6-1-2023

# Description: This script checks if the same file path exists multiple times, and prevents the same information to be added to files table in cmdb database. Prompts the user to pick an option whether wants to update or not.

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

# Function to check if file path already exists in the database
def check_file_exists(cursor, file_path):
    try:
        select_query = "SELECT COUNT(*) FROM files WHERE path = %s"
        cursor.execute(select_query, (file_path,))
        count = cursor.fetchone()[0]
        return count > 0
    except pymysql.Error as err:
        print(f"Error checking file existence in the database: {err}")
        return False

# Function to calculate md5 hashes
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

# Function to update file hash in the database
def update_file_hash(cursor, conn, file_path, file_hash):
    try:
        update_query = "UPDATE files SET hash = %s WHERE path = %s"
        update_values = (file_hash, file_path)
        cursor.execute(update_query, update_values)
        conn.commit()
        print("File hash updated successfully.")
    except pymysql.Error as err:
        print(f"Error updating file hash in the database: {err}")

# Function to insert file data into the database
def insert_file_data(cursor, conn, timestamp, file_path, file_hash):
    try:
        insert_query = "INSERT INTO files (timestamp, path, hash) VALUES (%s, %s, %s)"
        insert_values = (timestamp, file_path, file_hash)
        cursor.execute(insert_query, insert_values)
        conn.commit()
        print("Data inserted successfully.")
    except pymysql.Error as err:
        print(f"Error inserting data into 'files' table: {err}")

# Function to close the database connection
def close_database_connection(cursor, conn):
    cursor.close()
    conn.close()

# Main routine that is called when the script is run
def main():
    # Get the file path from the command-line argument
    if len(sys.argv) < 2:
        print("Please provide a file path as a command-line argument.")
        sys.exit(1)
    file_path = sys.argv[1]

    # Connect to the MySQL server
    conn, cursor = connect_to_database()

    # Get the current timestamp in ISO format
    timestamp = datetime.utcnow().isoformat(timespec='milliseconds')

    # Check if file path already exists in the database
    file_exists = check_file_exists(cursor, file_path)

    if file_exists:
        # Prompt user for update or skip
        user_input = input("File path already exists in the database. Do you want to update the hash? (Y/N): ")
        if user_input.lower() == 'y':
            # Calculate the MD5 hash of the file
            file_hash = calculate_md5_hash(file_path)
            if file_hash is None:
                close_database_connection(cursor, conn)
                sys.exit(1)
            # Update file hash in the database
            update_file_hash(cursor, conn, file_path, file_hash)
        else:
            print("File path won't be added to the database.")
            print("\nExiting.")
            close_database_connection(cursor, conn)
            sys.exit(0)
    else:
        # Calculate the MD5 hash of the file
        file_hash = calculate_md5_hash(file_path)
        if file_hash is None:
            close_database_connection
            sys.exit(1)

        # Insert the data into the 'files' table
        insert_file_data(cursor, conn, timestamp, file_path, file_hash)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
