import csv
import json


### Drivers Data

with open("./data/drivers.csv", 'r', newline='', encoding='utf-8') as driversCSV:
    reader = csv.reader(driversCSV)

    header = next(reader)

    drivers = {}
    for row in reader:
        name: str = f"{row[3]} {row[4]}"
        driver = {
            # "id": row[0],
            "name": name,
            "dob": row[5],
            "nationality": row[6]
        }
        drivers[row[0]] = driver

# drivers_file_name: str = "data/results_id.json"
# with open(drivers_file_name, 'w') as driverJSON:
#     json.dump(drivers, driverJSON, indent=4)


### Races Data

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

# races_file_name: str = "data/races.json"
# with open(races_file_name, 'w') as racesJSON:
#     json.dump(races, racesJSON, indent=4)


### Results Data

def fixRace(currentRace: list[dict]):
    for racer in currentRace:
        if racer[FINAL] == "\\N": racer[FINAL] = len(currentRace) + 1
        else: racer[FINAL] = int(racer[FINAL])
    currentRace.sort(key=lambda x: x[FINAL])

with open("./data/results.csv", 'r', encoding='utf-8') as resultsCSV:
    reader = csv.reader(resultsCSV)

    header = next(reader)
    ID: str = "id"
    NAME: str = "name"
    STANDING: str = "standing"
    QUALI: str = "qualifying"
    FINAL: str = "final"

    results: list[dict] = []
    currentID: str = "18"
    currentRace: list[dict] = []
    for row in reader:
        if row[1] != currentID:
            fixRace(currentRace)
            results.append({ID: currentID, STANDING: currentRace.copy()})
            currentID = row[1]
            currentRace.clear()

        currentRace.append({
            NAME: drivers[row[2]][NAME],
            QUALI: int(row[5]),
            FINAL: row[6]
        })

    fixRace(currentRace)
    results.append({ID: currentID, STANDING: currentRace.copy()})

# results_file_name: str = "data/results.json"
# with open(results_file_name, 'w') as resultsJSON:
#     json.dump(results, resultsJSON, indent=4)