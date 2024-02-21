import urllib

import requests
FLIGHT_API = "VeQ1nzuqN26LtW435wggy64vDpKv-Fki"
ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
HEADERS = {
    "apikey": FLIGHT_API,
    "Content-Type": "application/json"
}



class FlightSearch:

    #Search the code for the city we looking for
    def get_code(self, city_name):
        QUERY = {
            "term": f"{city_name}",
            "location_types":"city"
                }
        try:
            self.response = requests.get(url=ENDPOINT, headers=HEADERS, params=QUERY)
            self.response.raise_for_status()
            self.locations = self.response.json().get("locations",[])
            if self.locations:
                return self.locations[0].get("code",None)
            else:
                print(f"No locations found for {city_name}." )
                return None
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch airport code for {city_name}: {e}")
            return None