import csv
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft'

# send a GET request to the URL
response = requests.get(url)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# find the tables with class "wikitable sortable"
tables = soup.find_all('table', {'class': 'wikitable sortable'})

for i, table in enumerate(tables):
    # create a CSV file and write the data to it
    with open(f'fuel_efficiency_{i}.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # get the table headers
        headers = []
        for header in table.find_all('th'):
            headers.append(header.get_text().strip())
        writer.writerow(headers)

        # loop through the rows of the table
        for row in table.find_all('tr'):
            data = []

            # loop through the columns of each row
            for col in row.find_all('td'):
                # get the text content of the column
                data.append(col.get_text().strip())

            # write the row of data to the CSV file
            writer.writerow(data)