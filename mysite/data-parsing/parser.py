import csv
import sys
import requests
import json
def main():


    links = []

    for i in range(0, 300, 100):

        headers = { 'apikey': '52afcc10-91dc-11ea-8306-23ef3e34ef78' }

        params = (
            ("q","Refugee Camp"),
            ("tbm","nws"),
            ("device","desktop"),
            ("location","Manhattan,New York,United States"),
            ("num","100"),
            ("start", str(i))
        )

        print(i)

        response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params);

        json_string = json.loads(response.text)

        for r in json_string['news_results']:
            links.append(r['link'])

    print(links)


    f = open("entries2.txt", "w")
    countries = {
        'Ethiopia' : 'ET',
        'Kenya' : 'KY',

    }
    set = {}
    i = 0
    csvInfo = []

    #bangladesh

    with open(r'C:\Users\User\Desktop\Python Projects\Refugee Data\Data Sets\bangladesh.csv') as csvfile:

        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar = '|')
        for row in csvReader:
            
            newRow = []

            newRow.append(row['Camp Name'])
            newRow.append('BD')
            newRow.append(row['GPS_point_latitude'])
            newRow.append(row['GPS_point_longitude'])
            # print(newRow)
            csvInfo.append(newRow)

    #IDP - SY

    with open(r'C:\Users\User\Desktop\Python Projects\Refugee Data\Data Sets\IDP.csv') as csvfile:

        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar = '|')
        for row in csvReader:
            
            newRow = []

            newRow.append(row['Name'])
            newRow.append(row['fips'])
            newRow.append(row['Latitude'])
            newRow.append(row['Longitude'])
            # print(newRow)
            csvInfo.append(newRow)

    #Iraq

    with open(r'C:\Users\User\Desktop\Python Projects\Refugee Data\Data Sets\iraq.csv') as csvfile:

        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar = '|')
        for row in csvReader:
            
            newRow = []

            newRow.append(row['Name'])
            newRow.append('IQ')
            newRow.append(row['Latitude'])
            newRow.append(row['Longitude'])
            
            # print(newRow)
            csvInfo.append(newRow)

    # #Malawi

    with open(r'C:\Users\User\Desktop\Python Projects\Refugee Data\Data Sets\malawi.csv') as csvfile:

        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar = '|')
        for row in csvReader:
            
            newRow = []

            if('camp' in row['Site_Name'] or 'Camp' in row['Site_Name']):
                name = row['Site_Name']
                newName = name[:-4] + 'C' + name[-3:]
                newRow.append(newName)
                newRow.append('MW')
                newRow.append(row['LAT'])
                newRow.append(row['LONG'])
                # print(newRow)
                csvInfo.append(newRow)

    # #mali

    with open(r'C:\Users\User\Desktop\Python Projects\Refugee Data\Data Sets\mali.csv') as csvfile:

        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar = '|')
        for row in csvReader:
            
            newRow = []
            newRow.append(row['LOCATION_N'])
            newRow.append(row['COUNTRY_CO'])
            newRow.append(row['Latitude'])
            newRow.append(row['Longitude'])
            # print(newRow)
            csvInfo.append(newRow)

    # #west nile and east sudan

    with open(r'C:\Users\User\Desktop\Python Projects\Refugee Data\Data Sets\westnileeastsudan.csv') as csvfile:

        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar = '|')
        for row in csvReader:
            
            newRow = []
            newRow.append(row['Name'])
            newRow.append(row['State'])
            newRow.append(row['Lat'])
            newRow.append(row['Long'])
            # print(newRow)
            csvInfo.append(newRow)


    confirmRows = []
    j = 0
    for row in csvInfo:

        f.write('l = Location(city = "{}", state = "{}", lat = {}, lon = {}, geom = "POINT({} {})", reference = "{}")\n'.format(row[0], row[1], row[2], row[3], row[3], row[2], links[j]))
        f.write('l.save()\n')
        j += 1
    f.close()

if(__name__ == '__main__'):
    main()