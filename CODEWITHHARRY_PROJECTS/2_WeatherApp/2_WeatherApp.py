import requests
import json
import os
city = input("Enter the name of the city: \n")
url = f"https://api.weatherapi.com/v1/current.json?key=47633deab6094385854144129231704&q={city}"
r = requests.get(url)
print(r.text)
print(type(r.text))
wea_dic = json.loads(r.text)  # now convert type str to type dict by using json
w = wea_dic["current"]["temp_c"]
print(w)
print(type(wea_dic))

command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The current weather in {city} is {w} degrees')"
os.system(command)

command = f"The current weather in {city} is {w} degrees"
os.system(f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{command}')")


"""
{
    "location":{
        "name":"Delhi",
        "region":"Ontario",
        "country":"Canada",
        "lat":42.85,
        "lon":-80.5,
        "tz_id":"America/Toronto",
        "localtime_epoch":1681742872,
        "localtime":"2023-04-17 10:47"
    },

    "current":{
        "last_updated_epoch":1681742700,
        "last_updated":"2023-04-17 10:45",
        "temp_c":6.4,
        "temp_f":43.5,
        "is_day":1,
        "condition":{
            "text":"Sunny",
            "icon":"//cdn.weatherapi.com/weather/64x64/day/113.png",
            "code":1000
        },

        "wind_mph":10.5,
        "wind_kph":16.9,
        "wind_degree":200,
        "wind_dir":"SSW",
        "pressure_mb":1002.0,
        "pressure_in":29.59,
        "precip_mm":0.1,
        "precip_in":0.0,
        "humidity":75,
        "cloud":0,
        "feelslike_c":1.9,
        "feelslike_f":35.5,
        "vis_km":10.0,
        "vis_miles":6.0,
        "uv":2.0,
        "gust_mph":22.8,
        "gust_kph":36.7
    }
}
"""
