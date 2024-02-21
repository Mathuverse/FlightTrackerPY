import urllib

import requests
FLIGHT_API = "VeQ1nzuqN26LtW435wggy64vDpKv-Fki"
ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
HEADERS = {
    "apikey": FLIGHT_API,
    "Content-Type": "application/json"
}



class FlightSearch:

    def get_code(self, city_name):
        QUERY = {
            "term": f"{city_name}",
            "location_types":"city"
                }
        self.response = requests.get(url=ENDPOINT, headers=HEADERS, params=QUERY)
        return self.response.json()["locations"][0]["code"]