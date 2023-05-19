#!/usr/bin/python3
#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#5-17-2023

# Description - This program scans the wafeventlog file and creates a redirects.csv file that counts the numbers of times servers are redirected.

# Versioning
# Zoki: initial version v0.1

# Set up initial variables and imports
import re
from collections import defaultdict
import csv
# Read the log file
with open('wafeventlog', 'r') as file:
    lines = file.readlines()

# Initialize a dictionary to store the redirect counts
redirects = {}

# Iterate over the lines and extract the redirect URLs
for line in lines:
    match = re.search(r'REDIRECT: (.*?) to (https?://\S+)', line)
    if match:
        from_url = match.group(1)
        to_url = match.group(2)

        # Ignore redirects containing "Basic" or "ActiveSync"
        if "Basic" not in from_url and "ActiveSync" not in from_url:
            redirect_key = (from_url, to_url)
            redirects[redirect_key] = redirects.get(redirect_key, 0) + 1

# Sort the redirects by count in descending order
sorted_redirects = sorted(redirects.items(), key=lambda x: x[1], reverse=True)

# Write the redirects to a CSV file
with open('redirects.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Count', 'From', 'To'])
    writer.writerows([(count, from_url, to_url) for (from_url, to_url), count in sorted_redirects])

