import requests
GOOGLEENDPOINT="https://api.sheety.co/add06380239e9780950a2971b06b8efc/flightdeals/prices"

class DataManager:

    #When initialized requests a get for th sheet
    def __init__(self):
        self.response = requests.get(url=GOOGLEENDPOINT)
    #Get all the rows from the sheet prices
    def getData(self):
        return self.response.json()["prices"]
    #Update the value of one of the data
    def updateData(self,key,id,value):
        params={
            "price":{
                key:value
            }  
        }
        self.update = requests.put(url=f"{GOOGLEENDPOINT}/{id}",json=params)
        print(self.update.text)
