#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dataManager import DataManager
from flightData import FlightData
from flightSearch import FlightSearch
from notificationManager import NotificationManager

#Initialize the classes
data_man = DataManager()
email = NotificationManager()
flight_search = FlightSearch()
flight_data = FlightData()

#Fetch all the data from the sheet
google_data = data_man.getData()

#Iterate each destination in spreadsheet
for destination in google_data:
    #Check if the code is empty for the city 
    if destination.get("code", "") == "":
        code = flight_search.get_code(destination["city"])
        #If we find corresponding code for city update db
        if code:
            data_man.updateData("code", destination["id"], f"{code}")
            destination["code"] = code        
        else:
            continue

    #Check whatever the price is put it max to compare with
    if destination.get("lowestPrice", "") == "" or  destination.get("lowestPrice", "") >=0 :
        destination["lowestPrice"] = float("inf")

    #Get all the flight for the code
    flights = flight_data.get_flights_data(destination["code"])
    if not flights:
        continue

    #Cheapest price for all the flights for the code
    minPrice = float("inf")
    bestFlight = None
    for flight in flights:
        if flight["price"] < minPrice and flight["price"] < destination["lowestPrice"] :
            minPrice = flight["price"]
            bestFlight = flight
    #if we find best flight send an email to user with info and link to book
    if bestFlight:
        data_man.updateData("lowestPrice",destination["id"],bestFlight["price"])
        subject = "Low price Alert!"
        body = f"Low price found! Only {bestFlight['price']} CAD to fly from {bestFlight['flyFrom']} to {destination['city']}.\nBook here: {bestFlight['deep_link']}"
        email.sendEmail(subject,body)
print("Program completed")