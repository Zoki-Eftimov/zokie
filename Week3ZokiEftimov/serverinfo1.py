#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#4-27-2023

# Description

# Versioning
# Zoki 04 - 27 - 23: initial version v.01

# Import subprocess module, which provides a way to spawn new processes, and obtain thir return code (lets us integrate external programs into Python code).
import os
import subprocess

# Define function get_output that takes a command as input and executes it using the subprocess.run method with stdout and stderr; the standard output is returned as string while handling errors.
def get_output(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if stderr:
        raise Exception(f"Command {command} failed with error:\n{stderr.decode()}")
    return stdout.decode().strip()

# Defines the main function as the entry point of the script (then sets variable that will call the get_output function with the command as argument, and assigns the output to the variable)
def main():
    hostname = get_output("hostname")
    cpu_count = get_output("nproc")
    ram_gb = get_output("free -g | awk 'FNR == 2 {print $2}'")
    os_type = get_output("uname -s")
    os_version = get_output("uname -r")
    disk_count = get_output("lsblk -d | grep disk | wc -l")
    ip_address = get_output("ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1")
    mac_address = get_output("cat /sys/class/net/eth0/address")

# Prints the output and calls the variables defined in the function main
    print("*******************************")
    print("*\033[31mHostname:\033[0m", hostname)
    print("*\033[31mCPU (count):\033[0m", cpu_count)
    print("*\033[31mRAM (GB):\033[0m", ram_gb)
    print("*\033[31mOSType:\033[0m", os_type)
    print("*\033[31mOSVersion:\033[0m", os_version)
    print("*\033[31mDisks (Count):\033[0m", disk_count)
    print("*\033[31mip of eth0:\033[0m", ip_address)
    print("*\033[31mmac of eth0:\033[0m", mac_address)
    print("*******************************")
# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
