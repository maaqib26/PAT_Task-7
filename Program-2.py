"""
As discussed with Suman Gangopadhyay , For this task the restcountries site is down due to which not able to attempt the 1st
program. Have completed the 2nd program and below is the code
"""

import requests
from tabulate import tabulate


class openbrewery:
    def __init__(self, url) -> None:
        self.url = url

    def status_code(self):
        # Fetch the status code from the API to check if the request is successful
        response = requests.get(self.url)
        return response.status_code

    def fetch_brewery_data(self):
        # Fetch and return the data from the API if the status code is 200
        if self.status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "Error-404"

    def fetch_brewery_by_name(self):
        brewery_names = []

        # Print the names of the breweries if the status code is 200
        if self.status_code() == 200:
            print("Names of Breweries in State of" + " " + state + " " + "are:")
            for data in self.fetch_brewery_data():
                brewery_names.append([data['name']])

            # Create a list of rows for the table
            rows = [[state, name] for name in brewery_names]

            # Format the brewery names as a table using tabulate
            table = tabulate(rows, headers=["State", "Brewery Names"], tablefmt="fancy_grid")
            return table
        else:
            print("Error-404")

    def fetch_brewery_count(self):
        # Return the count of breweries in Alaska if the status code is 200
        if self.status_code() == 200:
            return "Count of Breweries in state of" + " " + state + " " + "are: {} \n ".format(len(self.fetch_brewery_data()))
        else:
            return "Error-404"
        
    def fetch_brewery_type(self):
        # Print the number and types of breweries in each city in Alaska if the status code is 200
        if self.status_code() == 200:
            print("The Number & Types of Breweries in each individual cities of" + " " + state + " " + "are: ")
            brewery_types_citywise = {}
            for data in self.fetch_brewery_data():
                city = data['city']
                brewery_type = data['brewery_type']
                if city not in brewery_types_citywise:
                    brewery_types_citywise[city] = {}
                if brewery_type not in brewery_types_citywise[city]:
                    brewery_types_citywise[city][brewery_type] = 0
                brewery_types_citywise[city][brewery_type] += 1

            rows = []
            for city, brewery_types in brewery_types_citywise.items():
                for brewery_type, count in brewery_types.items():
                    rows.append([city, brewery_type, count])

            table = tabulate(rows, headers=["City", "Brewery Type", "Count"], tablefmt="fancy_grid")
            return table

        else:
            return "Error-404"

    def fetch_brewery_with_website(self):
        # Fetch and return the names of breweries with websites in Alaska, along with the count
        count = 0
        website_data = []
        if self.status_code() == 200:
            for data in self.fetch_brewery_data():
                if data['website_url'] and data['website_url'] != 'null':
                    count += 1
                    website_data.append(data['name'])
            # Return the formatted string with count and names
            return "There are total {} breweries with website in state of {} and those are:\n {}".format(count, state, '\n'.join(website_data))
        else:
            return "Error-404"

if __name__ == "__main__":
    # Define the URL for the API request
    states = ["alaska","maine","new york"]

    for state in states:
        # Create an instance of the openbrewery class
        url = "https://api.openbrewerydb.org/v1/breweries?by_state="+state+"&per_page=3"
        #print(url)
        brewery_data = openbrewery(url)

        # Fetch the data and print the breweries with websites
        #print(brewery_data.status_code())
        #brewery_data.fetch_brewery_data()
        print(brewery_data.fetch_brewery_by_name())
        print(brewery_data.fetch_brewery_count())
        print(brewery_data.fetch_brewery_with_website())
        print(brewery_data.fetch_brewery_type())
