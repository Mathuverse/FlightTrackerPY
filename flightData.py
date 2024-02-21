import requests
import datetime as d

FLIGHT_API = "VeQ1nzuqN26LtW435wggy64vDpKv-Fki"
FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HEADERS = {
    "apikey" : FLIGHT_API,
    "Content-Type" : "application/json"
}

class FlightData:

    #Sets the location from which city your travelling and get ready the time from tomorrow to in 6 months
    def __init__(self):
        self.departure_code = "YMQ"
        self.departure_city = "Montreal"
        self.price = 0
        self.tomorrow = (d.datetime.today() + d.timedelta(days=1)).strftime("%d/%m/%Y")
        self.in_six_months= (d.datetime.today() + d.timedelta(days=6*30)).strftime("%d/%m/%Y")

    #The code for the location from which your travelling to is in the parameters
    def get_flights_data(self,code):
        QUERY = {
            "fly_from": "YMQ",
            "fly_to": f"{code}",
            "date_from": f"{self.tomorrow}",
            "date_to": f"{self.in_six_months}",
            "curr": "CAD"
        }
        
        try:
            self.response = requests.get(url=FLIGHT_ENDPOINT, headers=HEADERS, params=QUERY)
            self.response.raise_for_status()
            data = self.response.json().get("data",[])
            return data if data else None
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch flight data: {e}")
            return None

        
