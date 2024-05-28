import requests

class openbrewery:
    def __init__(self, url) -> None:
        self.url = url

    def status_code(self):
        response = requests.get(self.url)
        return response.status_code

    # def check_access(self):
    #     code = self.status_code()
    #     if code == 200:
    #         print("Access")
    #     elif code == 404:
    #         print("Error-404")
    #     else:
    #         print("Error")

    def fetch_alaska_brewery(self):
        if self.status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "Error-404"

    def fetch_alaska_brewery_by_name(self):
        if self.fetch_alaska_brewery():
            for data in self.fetch_alaska_brewery():
                print(data.get('name'))
        else:
            print("No API Data Present")

    def fetch_alaska_brewery_count(self):
        if self.status_code() == 200:
            return len(self.fetch_alaska_brewery())
        else:
            return "Error-404"

    # def fetch_alaska_brewery_type(self):
    #     temp_dict = {}
    #     if self.fetch_alaska_brewery():
    #         for data in self.fetch_alaska_brewery():
    #             temp_dict.update({data['city']:data['brewery_type']})
    #     print(temp_dict)
    #     for key,value in temp_dict.items():
    #         print(f"{key}:{value}")
    #     print(len(temp_dict))
    #             #print(data.keys())
    #
    #             #print(data.get('city') + " " + data.get('brewery_type'))
    #
    #     # else:
    #     #     print("No API Data Present")

    def fetch_brewery_with_website(self):
        count = 0
        website_data = []
        if self.fetch_alaska_brewery():
            for data in self.fetch_alaska_brewery():
                if data['website_url'] and data['website_url']!='null':
                    print(data['name'])
                    count += 1
                    website_data.append(data['name'])

        print('There are total {} breweries with website and those are {}.'.format(count,', '.join(website_data)))


if __name__ == "__main__":

    url = "https://api.openbrewerydb.org/v1/breweries?by_state=alaska&per_page=20"

    brewery_data = openbrewery(url)

    #print(brewery_data.status_code())
    #print(brewery_data.fetch_alaska_brewery())
    brewery_data.fetch_alaska_brewery_by_name()
    print(brewery_data.fetch_alaska_brewery_count())
    #brewery_data.fetch_alaska_brewery_type()
    brewery_data.fetch_brewery_with_website()
    #brewery_data.check_access()

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
