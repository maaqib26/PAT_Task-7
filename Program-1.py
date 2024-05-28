import requests

class restcountries:
    def __init__(self,url) -> None:
        self.url = url
        
    def fetch_data(self):
        code = requests.get(self.url)
        return code.status_code 
        response = requests.get(self.url).json()
        return response
    
if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    #url = "https://62513902977373573f4567fb.mockapi.io/pizza/pizza_names"
    countries_info = restcountries(url)
    print(countries_info.fetch_data())
    


    


   
        


        
