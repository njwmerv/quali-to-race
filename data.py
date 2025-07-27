import csv
import json

# with open("./data/drivers.csv", 'r', newline='', encoding='utf-8') as driversCSV:
#     reader = csv.reader(driversCSV)
#
#     header = next(reader)
#
#     drivers = {}
#     for row in reader:
#         name: str = f"{row[3]} {row[4]}"
#         driver = {
#             # "id": row[0],
#             "name": name,
#             "dob": row[5],
#             "nationality": row[6]
#         }
#         drivers[row[0]] = driver

# drivers_file_name: str = "data/results_id.json"
# with open(drivers_file_name, 'w') as driverJSON:
#     json.dump(drivers, driverJSON, indent=4)

with open("./data/races.csv", 'r', encoding='utf-8') as racesCSV:
    reader = csv.reader(racesCSV)

    header = next(reader)

    races = {}
    for row in reader:
        race = {
            "year": row[1],
            "name": row[4],
            "full_name": f"{row[1]} {row[4]}",
            "round": row[2],
            "date": row[5]
        }
        races[row[0]] = race
    print(races)

races_file_name: str = "data/races.json"
with open(races_file_name, 'w') as racesJSON:
    json.dump(races, racesJSON, indent=4)