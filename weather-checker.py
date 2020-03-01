#!/usr/bin/env python
# weather checker by nomudnolotus
import requests
import json
import sys

def getWeather():
    api_key = "2132fba1d42920258ae8df826a993528" #enter api key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = str(sys.argv[1])
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        kelvintof = str(((current_temperature) - 273.15) * 9/5 + 32)
        weatherData = { #stores data in dict for future funcs
            "current_temperature": str(kelvintof),
            "current_pressure" : str(current_pressure),
            "current_humidity": str(current_humidity),
            "weather_description": str(weather_description)
        }
    return weatherData

def main():
    weatherData = getWeather()
    print("Temperature: (F)" + weatherData["current_temperature"] + "\n" \
        "Atmospheric Pressure (in hPa): " + weatherData["current_pressure"] + "\n" \
        "Humidity (percentage): " + weatherData["current_humidity"] + "\n" \
        "Description: " + weatherData["weather_description"] + "\n")

if __name__ == "__main__":
    if (len(sys.argv) < 1):
        print("error: enter arg1(city)")
    main()
