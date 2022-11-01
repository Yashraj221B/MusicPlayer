import json
import requests
##<!-- This File is Under Production So It may Contain bugs --!>##


def getWeather():
    api = "gw0brHCdajgtm1Y7pbodIwzaRSziExm1"
    url = f"https://dataservice.accuweather.com/currentconditions/v1/204843?apikey={api}&q&details=true"
    data = json.load(open("data.json"))[0]  # requests.get(url).content)[0]
    # print(data)
    print("Temperature:", data["Temperature"]["Metric"]["Value"])
    print("WeatherText:", data["WeatherText"])
    print("Visiblity:", data["Visibility"]["Metric"]["Value"])
    print("Dew Point:",data["DewPoint"]["Metric"]["Value"])
    print("Pressure:",data["Pressure"]["Metric"]["Value"])
    print("Wind:",data["Wind"]["Speed"]["Metric"]["Value"],"Km/h ",data["Wind"]["Direction"]["English"])
    print("Humidity:",data["RelativeHumidity"])
    print("UV Index:",data["UVIndex"],data["UVIndexText"])


if __name__ == "__main__":
    getWeather()
