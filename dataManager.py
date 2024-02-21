import requests
GOOGLEENDPOINT="https://api.sheety.co/add06380239e9780950a2971b06b8efc/flightdeals/prices"

class DataManager:

    #When initialized requests a get for th sheet
    def __init__(self):
        try:
            self.response = requests.get(url=GOOGLEENDPOINT)
            self.response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data: {e}")
            self.response = None

    #Get all the rows from the sheet prices
    def getData(self):
        if self.response is not None:
            try:
                data = self.response.json().get("prices",[])
                return data
            except ValueError as e:
                print(f"Failed to parse data: {e}")
                return []
        # return self.response.json()["prices"]
        else:
            print("No data available.")
            return []
        
    #Update the value of one of the data
    def updateData(self,key,id,value):
        params={
            "price":{
                key:value
            }  
        }
        try:
            self.update = requests.put(url=f"{GOOGLEENDPOINT}/{id}",json=params)
            self.update.raise_for_status()
            print("Update successful")
        except requests.exceptions.RequestException as e:
            print(f"Failed to update data: {e}")
    

