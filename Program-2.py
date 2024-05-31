# import requests
#
# class openbrewery:
#     def __init__(self, url) -> None:
#         self.url = url
#
#     def status_code(self):
#         response = requests.get(self.url)
#         return response.status_code
#
#     def fetch_alaska_brewery(self):
#         if self.status_code() == 200:
#             return requests.get(self.url).json()
#         else:
#             return "Error-404"
#
#     def fetch_alaska_brewery_by_name(self):
#         if self.status_code() == 200:
#             print("Names of Breweries in State of Alaska are:")
#             for data in self.fetch_alaska_brewery():
#                 brewery_names = data['name']
#                 print(brewery_names)
#         else:
#             print("Error-404")
#
#     def fetch_alaska_brewery_count(self):
#         if self.status_code() == 200:
#             return "Count of Breweries in State of Alaska are: {} ".format(len(self.fetch_alaska_brewery()))
#         else:
#             return "Error-404"
#
#     def fetch_alaska_brewery_type(self):
#         if self.status_code() == 200:
#             print("The Number & Types of Breweries in each individual cities of Alaska are: ")
#             brewery_types_citywise = {}
#             for data in self.fetch_alaska_brewery():
#                 city = data['city']
#                 brewery_type = data['brewery_type']
#                 if city not in brewery_types_citywise:
#                     brewery_types_citywise[city] = {}
#                 if brewery_type not in brewery_types_citywise[city]:
#                     brewery_types_citywise[city][brewery_type] = 0
#                 brewery_types_citywise[city][brewery_type] += 1
#
#             for city, brewery_types in brewery_types_citywise.items():
#                 print(f"City: {city}")
#                 for brewery_type, count in brewery_types.items():
#                     print(f"  {brewery_type}: {count}")
#         else:
#             return "Error-404"
#
#     def fetch_brewery_with_website(self):
#         count = 0
#         website_data = []
#         if self.status_code() == 200:
#             for data in self.fetch_alaska_brewery():
#                 if data['website_url'] and data['website_url']!='null':
#                     count += 1
#                     website_data.append(data['name'])
#             return 'There are total {} breweries with website and those are \n {}.'.format(count,'\n'.join(website_data))
#         else:
#             return "Error-404"
#
# if __name__ == "__main__":
#
#     url = "https://api.openbrewerydb.org/v1/breweries?by_state=alaska&per_page=20"
#
#     brewery_data = openbrewery(url)
#
#     #print(brewery_data.status_code())
#     brewery_data.fetch_alaska_brewery()
#     #brewery_data.fetch_alaska_brewery_by_name()
#     #print(brewery_data.fetch_alaska_brewery_count())
#     #brewery_data.fetch_alaska_brewery_type()
#     print(brewery_data.fetch_brewery_with_website())

import requests

class openbrewery:
    def __init__(self, url) -> None:
        # Initialize the class with the URL
        self.url = url

    def status_code(self):
        # Fetch the status code from the API to check if the request is successful
        response = requests.get(self.url)
        return response.status_code

    def fetch_alaska_brewery(self):
        # Fetch and return the data from the API if the status code is 200
        if self.status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "Error-404"

    def fetch_alaska_brewery_by_name(self):
        # Print the names of the breweries in Alaska if the status code is 200
        if self.status_code() == 200:
            print("Names of Breweries in State of Alaska are:")
            for data in self.fetch_alaska_brewery():
                brewery_names = data['name']
                print(brewery_names)
            print("\n")
        else:
            print("Error-404")

    def fetch_alaska_brewery_count(self):
        # Return the count of breweries in Alaska if the status code is 200
        if self.status_code() == 200:
            return "Count of Breweries in State of Alaska are: {} \n ".format(len(self.fetch_alaska_brewery()))
        else:
            return "Error-404"


    def fetch_alaska_brewery_type(self):
        # Print the number and types of breweries in each city in Alaska if the status code is 200
        if self.status_code() == 200:
            print("The Number & Types of Breweries in each individual cities of Alaska are: ")
            brewery_types_citywise = {}
            for data in self.fetch_alaska_brewery():
                city = data['city']
                brewery_type = data['brewery_type']
                if city not in brewery_types_citywise:
                    brewery_types_citywise[city] = {}
                if brewery_type not in brewery_types_citywise[city]:
                    brewery_types_citywise[city][brewery_type] = 0
                brewery_types_citywise[city][brewery_type] += 1

            # Print the results
            for city, brewery_types in brewery_types_citywise.items():
                print(f"City: {city}")
                for brewery_type, count in brewery_types.items():
                    print(f"  {brewery_type}: {count}")
            print("\n")
        else:
            return "Error-404"

    def fetch_brewery_with_website(self):
        # Fetch and return the names of breweries with websites in Alaska, along with the count
        count = 0
        website_data = []
        if self.status_code() == 200:
            for data in self.fetch_alaska_brewery():
                if data['website_url'] and data['website_url'] != 'null':
                    count += 1
                    website_data.append(data['name'])
            # Return the formatted string with count and names
            return 'There are total {} breweries with website and those are:\n{}'.format(count, '\n'.join(website_data))
        else:
            return "Error-404"

if __name__ == "__main__":
    # Define the URL for the API request
    url = "https://api.openbrewerydb.org/v1/breweries?by_state=alaska&per_page=20"

    # Create an instance of the openbrewery class
    brewery_data = openbrewery(url)

    # Fetch the data and print the breweries with websites
    #print(brewery_data.status_code())
    brewery_data.fetch_alaska_brewery_by_name()
    print(brewery_data.fetch_alaska_brewery_count())
    brewery_data.fetch_alaska_brewery_type()
    print(brewery_data.fetch_brewery_with_website())



# import requests
# from collections import defaultdict
#
# # Fetch data from the API
# response = requests.get("https://api.openbrewerydb.org/v1/breweries?by_state=alaska&per_page=50")
# data = response.json()
#
# # Initialize a dictionary to hold the counts
# city_brewery_types = defaultdict(lambda: defaultdict(int))
#
# # Process the data
# for brewery in data:
#     city = brewery['city']
#     brewery_type = brewery['brewery_type']
#     city_brewery_types[city][brewery_type] += 1
#
# # Print the results
# for city, types in city_brewery_types.items():
#     print(f"City: {city}")
#     for brewery_type, count in types.items():
#         print(f"  {brewery_type}: {count}")
