import csv
import dns.resolver

def validate_dns_record(name, record_type, expected_value):
    try:
        answers = dns.resolver.resolve(name, record_type)
        for rdata in answers:
            if expected_value in rdata.to_text():
                print(f"Record {name} {record_type} is valid.")
                return True
        print(f"Record {name} {record_type} is invalid. Expected: {expected_value}")
        return False
    except Exception as e:
        print(f"Error validating record {name} {record_type}: {e}")
        return False

input_file = 'TXT.csv'

with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    
    for row in reader:
        name, ttl, record_type, record = row[:4]
        validate_dns_record(name, record_type, record)