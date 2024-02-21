import requests

#Your API KEY
API_KEY = "73d9835cafa107d657dbfacb2261e0e0"

def getData(location, forecast_days=None):
    
    #Change API_KEY using your API_KEY
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    
    response = requests.get(url) #Sending request
    
    data = response.json() #Get response
    
    filtered_data = data["list"]
    nr_values = 8 * forecast_days #Free plan API provide only 40 values for 5 days 8 for 24 hours
    filtered_data = filtered_data[:nr_values]
    
    
    return filtered_data

if __name__ == "__main__":
    print(getData(location="Tokyo", forecast_days=3))