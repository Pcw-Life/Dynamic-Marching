#!/usr/bin/env python3

# Define the input and output file paths
input_file = 'zone.txt'
output_file = 'zone.bind'

# Function to format a record into BIND format
def format_record(fields):
    name, ttl, dns_class, record_type, *target = fields
    target = ' '.join(target)
    if record_type == 'SOA':
        # Handle multiline SOA record
        soa_components = target.replace('(', '').replace(')', '').split()
        if len(soa_components) < 7:
            raise ValueError(f"SOA record has an incorrect number of components: {soa_components}")
        mname, rname, serial, refresh, retry, expire, minimum = soa_components[:7]
        return (f"{name} {ttl} {dns_class} {record_type} {mname} {rname} (\n"
                f"    {serial} ; Serial\n"
                f"    {refresh} ; Refresh\n"
                f"    {retry} ; Retry\n"
                f"    {expire} ; Expire\n"
                f"    {minimum} ; Minimum TTL\n"
                f")")
    else:
        return f"{name} {ttl} {dns_class} {record_type} {target}"

try:
    # Open the input text file for reading
    with open(input_file, 'r') as infile:
        # Open the output file for writing
        with open(output_file, 'w') as outfile:
            # Initialize a buffer for multiline SOA records
            buffer = []
            for line in infile:
                # Split the line into fields
                fields = line.split()
                
                # Check if the line is part of a multiline SOA record
                if 'SOA' in fields and '(' in line:
                    buffer = fields
                    continue
                elif buffer:
                    buffer.extend(fields)
                    if ')' in line:
                        fields = buffer
                        buffer = []
                    else:
                        continue
                
                # Check if the line has the correct number of fields
                if len(fields) >= 5:
                    # Format the record and write to the output file
                    formatted_record = format_record(fields)
                    outfile.write(formatted_record + '\n')
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)