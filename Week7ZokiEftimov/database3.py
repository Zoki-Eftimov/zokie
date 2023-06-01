#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-30-2023

# Description - This script is getting a server information and writing/appending to mysql database cmdb table device

# Versioning
# Zoki: initial version v.0.1

# Set up initial variables and imports
import pymysql
import subprocess
import sys

#This function gets the serverinfo based on the script serverinfo1 (At first, I wrote a script that will import serverinfo1, but I realized I don't have to do that, so I implemented serverinfo1 here).
def get_server_info():
    server_info = {}
    server_info['name'] = get_output("whoami")
    server_info['CPU'] = get_output("nproc")
    server_info['RAM'] = get_output("free -g | awk 'FNR == 2 {print $2}'")
    server_info['OSType'] = get_output("uname -s")
    server_info['OSVersion'] = get_output("uname -r")
    server_info['Disks'] = get_output("lsblk -d | grep disk | wc -l")
    server_info['IP'] = get_output("ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1")
    server_info['MAC'] = get_output("cat /sys/class/net/eth0/address")
    return server_info

#This function executes a command in the shell and captures the output
def get_output(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if stderr:
        raise Exception(f"Command '{command}' failed with error:\n{stderr.decode().strip()}")
    return stdout.decode().strip()

#Function to connect to the mysql database
def connect_to_database():
    host = 'localhost'
    user = 'root'
    password = 'password'
    database = 'cmdb'
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        return connection, cursor
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

# Function to insert server information into the database
def insert_server_info(name, macaddress, ip, cpucount, disks, ram, ostype, osversion):
    connection, cursor = connect_to_database()
    try:
        # Prepare the SQL query
        sql = "INSERT INTO device (name, macaddress, ip, cpucount, disks, ram, ostype, osversion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, macaddress, ip, cpucount, disks, ram, ostype, osversion)
        cursor.execute(sql, val)
        connection.commit()
    except Exception as e:
        # Rollback in case of any error
        connection.rollback()
        raise e
    finally:
        # Close the database connection
        connection.close()

#Main function that calls the rest of the functions
def main():
    # Call the main function from serverinfo1.py to retrieve the server information
    server_info = get_server_info()
    # Extract the server information
    name = server_info['name']
    cpucount = server_info['CPU']
    ram = server_info['RAM']
    ostype = server_info['OSType']
    osversion = server_info['OSVersion']
    disks = server_info['Disks']
    ip = server_info['IP']
    macaddress = server_info['MAC']

    # Insert the server information into the database
    insert_server_info(name, macaddress, ip, cpucount, disks, ram, ostype, osversion)
    print("Server info appended successfully!")
# Run main() if script called directly
if __name__ == "__main__":
    main()

