# # # Given dictionary
# # temp_dict = {'Healy': 'micro', 'Anchorage': 'brewpub', 'Juneau': 'regional'}
#
# # # Initialize a dictionary to hold the counts
# # value_counts = {}
#
# # # Count the occurrences of each value
# # for key, value in temp_dict.items():
#     # if value in value_counts:
#         # value_counts[value] += 1
#     # else:
#         # value_counts[value] = 1
#
# # print(value_counts)
# # # Print the results
# # for value, count in value_counts.items():
#     # print(f"{value}: {count}")
#
# # Given dictionary
# temp_dict = {'Healy': 'micro', 'Anchorage': 'brewpub', 'Juneau': 'regional'}
#
# # Initialize dictionaries to hold the counts
# key_counts = {}
# value_counts = {}
#
# # Count the occurrences of each key and value
# for key, value in temp_dict.items():
#     # Count keys
#     if key in key_counts:
#         key_counts[key] += 1
#     else:
#         key_counts[key] = 1
#
#     # Count values
#     if value in value_counts:
#         value_counts[value] += 1
#     else:
#         value_counts[value] = 1
#
# # Print the results
# print("Key counts:")
# for key, count in key_counts.items():
#     print(f"{key}: {count}")
#
# print("\nValue counts:")
# for value, count in value_counts.items():
#     print(f"{value}: {count}")

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

# import requests
#
# # Fetch data from the API
# response = requests.get("https://api.openbrewerydb.org/v1/breweries?by_state=alaska&per_page=50")
# data = response.json()
#
# # Initialize a dictionary to hold the counts
# city_brewery_types = {}
#
# # Process the data
# for brewery in data:
#     city = brewery['city']
#     brewery_type = brewery['brewery_type']
#     if city not in city_brewery_types:
#         city_brewery_types[city] = {}
#     if brewery_type not in city_brewery_types[city]:
#         city_brewery_types[city][brewery_type] = 0
#     city_brewery_types[city][brewery_type] += 1

import requests


class BreweryFetcher:
    def fetch_alaska_brewery(self):
        response = requests.get("https://api.openbrewerydb.org/v1/breweries?by_state=alaska&per_page=3")
        if response.status_code == 200:
            return response.json()
        return []

    def fetch_brewery_with_website(self):
        breweries = self.fetch_alaska_brewery()
        breweries_with_websites = [brewery['name'] for brewery in breweries if brewery['website_url']]

        # Format and print the message
        print("There are total {} breweries with website and those are {}".format(
            len(breweries_with_websites), ', '.join(breweries_with_websites)
        ))


# Example usage
fetcher = BreweryFetcher()
fetcher.fetch_brewery_with_website()




