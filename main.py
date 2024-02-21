#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dataManager import DataManager
from flightData import FlightData
from flightSearch import FlightSearch
from notificationManager import NotificationManager

data_man = DataManager()
google_data = data_man.getData()
email = NotificationManager()
# print(google_data)

flight_search = FlightSearch()
flight_data = FlightData()

for dic in google_data:
    min = 1000000
    msg=""
    print(dic )
    flights= flight_data.get_flights_data(dic["code"])
    for f in flights:

        # print(f)dic["lowestPrice"]
        if f["price"] <= min and f["price"] < dic["lowestPrice"]:
            min = f["price"]
            msg = f"Subject: AIRPLANE PRICES \n\n FROM: {f['flyFrom']} TO: {f['flyTo']} price : {f['price']} {f['deep_link']}"
            msg.encode("utf-8")
            email.sendEmail(msg)


for dic in google_data:
    if dic["code"]=="":
        code = flight_search.get_code(dic["city"])
        data_man.updateData("code", dic["id"], f"{code}")