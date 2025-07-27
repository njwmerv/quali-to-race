import csv
import json

with open("./data/drivers.csv", 'r', newline='', encoding='utf-8') as driversCSV:
    reader = csv.reader(driversCSV)

    header = next(reader)
    ID: str = 'id'
    NAME: str = 'name'
    DOB: str = header[5]
    NATIONALITY: str = header[6]

    drivers = {}
    for row in reader:
        name: str = f"{row[3]} {row[4]}"
        driver = {
            # ID: row[0],
            NAME: name,
            DOB: row[5],
            NATIONALITY: row[6]
        }
        drivers[row[0]] = driver

drivers_file_name: str = "data/drivers_id.json"

with open(drivers_file_name, 'w') as driverJSON:
    json.dump(drivers, driverJSON, indent=4)
