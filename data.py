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

def fixRace(race):
    for racer in race[FINAL]:
        if racer[POS] == "\\N": racer[POS] = len(race[FINAL]) + 1
        else: racer[POS] = int(racer[POS])
    race[QUALI].sort(key=lambda x: x[POS])
    race[FINAL].sort(key=lambda x: x[POS])

with open("./data/results.csv", 'r', encoding='utf-8') as resultsCSV:
    reader = csv.reader(resultsCSV)

    header = next(reader)
    QUALI: str = "qualifying"
    FINAL: str = "final"
    NAME: str = "name"
    POS: str = "pos"

    results = []
    currentRace = "18"
    race = {QUALI:[], FINAL:[]}
    for row in reader:
        if row[1] != currentRace:
            currentRace = row[1]
            results.append(race)
            race[QUALI].clear()
            race[FINAL].clear()
        driverName: str = drivers[row[2]][NAME]
        race[QUALI].append({NAME: driverName, POS: int(row[5])})
        race[FINAL].append({NAME: driverName, POS: row[6]})
    fixRace(race)
    results.append(race)

# results_file_name: str = "data/results.json"
# with open(results_file_name, 'w') as resultsJSON:
#     json.dump(results, resultsJSON, indent=4)