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
            #return requests.get(self.url).json()
            return len(requests.get(self.url).json())
        else:
            return "Error-404"
        
    def fetch_alaska_brewery_by_name(self):
        for data in self.fetch_alaska_brewery():
            print(data.get('name'))
            


if __name__ == "__main__":

    url = "https://api.openbrewerydb.org/v1/breweries?by_state=alaska&per_page=3"
    

    brewery_data = openbrewery(url)

    #print(brewery_data.status_code())
    print(brewery_data.fetch_alaska_brewery())
    brewery_data.fetch_alaska_brewery_by_name()
    #brewery_data.check_access()