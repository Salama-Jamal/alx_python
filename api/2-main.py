import csv

# Sample data
data = [
    {'Name': 'John', 'Age': 30, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 25, 'City': 'San Francisco'},
    {'Name': 'Bob', 'Age': 35, 'City': 'Los Angeles'},
]

# CSV filename
csv_filename = 'sample_data.csv'

# Writing to CSV
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Writing header
    writer.writeheader()

    # Writing data
    writer.writerows(data)

print(f"The CSV file '{csv_filename}' was successfully created.")
