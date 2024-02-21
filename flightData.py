import requests
import datetime as d

FLIGHT_API = "VeQ1nzuqN26LtW435wggy64vDpKv-Fki"
FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HEADERS = {
    "apikey" : FLIGHT_API,
    "Content-Type" : "application/json"
}

class FlightData:

    def __init__(self):
        self.departure_code = "YMQ"
        self.departure_city = "Montreal"
        self.price = 0
        self.tomorrow = (d.datetime.today() + d.timedelta(days=1)).strftime("%d/%m/%Y")
        self.in_six_months= (d.datetime.today() + d.timedelta(days=6*30)).strftime("%d/%m/%Y")
#lol
