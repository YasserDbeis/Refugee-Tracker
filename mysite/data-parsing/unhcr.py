import json
import csv

nameAndPop = {}

geojson = open("final6.geo.json", "w")

countries = []

with open(r'C:\Users\User\Desktop\Python Projects\Refugee Data\Data Sets\countrypopsCSV.csv') as csvfile:

    csvReader = csv.DictReader(csvfile, delimiter=',', quotechar = '|')
    for row in csvReader:
        pop = {}

        countryName = row['origin']
        population = row['refugeePop']
        countries.append(countryName)
        nameAndPop[countryName] = population
        

with open('countries-hires.json') as f:
    data = json.load(f)

    for i in range(len(data["features"])):
        properties = data["features"][i]["properties"]
        if(properties['ADMIN'] in countries):
            tempJson = (data['features'][i])
            tempJson['properties']['population'] = int(nameAndPop[properties['NAME']])
            geojson.write(str(tempJson) + ",\n")
        else:
            print(properties['ADMIN'])
            # print(str(data['features'][i]))

# for line in data['features']:
#     if(line['properties']['ADMIN'] in pop.keys()):





        # print("hey")
        # tempJson = json.loads(line)
        # tempJson['properties']['population'] = pop[line['properties']['ADMIN']]
        # newJsonStr = json.dumps(tempJson)
        # geojson.write(newJsonStr)