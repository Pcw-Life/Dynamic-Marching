#!/usr/bin/env python3
import csv
import os

# Define the input and output file paths
input_file = 'zone.txt'
output_file = 'zone.csv'

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Error: The file '{input_file}' does not exist.")
    exit(1)

try:
    # Open the input file for reading
    with open(input_file, 'r') as infile:
        # Open the output file for writing
        with open(output_file, 'w', newline='') as outfile:
            # Define the CSV writer
            writer = csv.writer(outfile)
            
            # Write the header row
            writer.writerow(['Name', 'TTL', 'Class', 'Type', 'Target'])
            
            # Read each line from the input file
            for line in infile:
                # Split the line into fields
                fields = line.split()
                
                # Check if the line has the correct number of fields
                if len(fields) >= 5:
                    # Extract the relevant fields
                    name = fields[0]
                    ttl = fields[1]
                    dns_class = fields[2]
                    record_type = fields[3]
                    target = ' '.join(fields[4:])
                    
                    # Write the fields to the CSV file
                    writer.writerow([name, ttl, dns_class, record_type, target])
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)