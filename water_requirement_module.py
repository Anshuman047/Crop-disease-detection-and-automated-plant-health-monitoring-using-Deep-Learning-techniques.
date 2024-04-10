import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def categorize_humidity(humidity):
    if humidity < 25:
        return "DESERT"
    elif 25 <= humidity < 40:
        return "SEMI ARID"
    elif 40 <= humidity < 60:
        return "SEMI HUMID"
    else:
        return "HUMID"
        
#Used weather codes to wrapping up them into common headings
def categorize_weather(weather_code):
    rain_codes = [
        200, 201, 202, 210, 211, 212, 221, 230, 231, 232,  # Thunderstorm
        
        300, 301, 302, 310, 311, 312, 313, 314, 321, # Drizzle
        
        500, 501, 502, 503, 504, 511, 520, 521, 522, 531 # Rain
    ]
    normal_codes = [
        701, 711, 721, 731, 741, 751, 761, 762, 771, # Atmosphere
        
        801, 802, 803, 804 # clouds
    ]
    sunny_codes = [
        800 #clear
    ]
    wind_codes = [
       781 # Turnado
    ]
    
    if weather_code in rain_codes:
        return "RAINY"
    elif weather_code in normal_codes:
        return "NORMAL"
    elif weather_code in sunny_codes:
        return "SUNNY"
    elif weather_code in wind_codes:
        return "WINDY"
    else:
        return "Unknown"

path = "/home/Water_Requirement_Dataset.csv"

df = pd.read_csv(path)

def water_requirement(crop_type,temp,soil_type,region,weather):
    return (df['WATER REQUIREMENT'].where(df["CROP TYPE"] == crop_type).where(df["TEMPERATURE"] == temp).where(
        df["SOIL TYPE"] == soil_type).where(df["REGION"] == region).where(
        df["WEATHER CONDITION"] == weather).dropna()).item()


# This function would execute api-call and fetch required informations
def weatherForecaste(api_key, cityName, crop_type, soil_type):
    import requests
    from datetime import datetime
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temperature = data['main']['temp'] #Temperature
        humidity = data['main']['humidity'] #Humidity %
        description = data['weather'][0]['description'] #Weather-condition
        
        weather_conditions = data.get('weather', []) #This would fetch the weather-condition's codes used for weatherCondition categorisation 
        for condition in weather_conditions:
            weather_code = condition.get('id')
            
    
        # Conversion of temperature from Kelvin to Celsius
        temperature_celsius = temperature - 273.15
        if(temperature_celsius < 20):
            temp = "10-20"
        elif(temperature_celsius < 30):
            temp = "20-30"
        elif(temperature_celsius < 30):
            temp = "30-40"
        else:
            temp = "40-50"

        # For humidity
        category = categorize_humidity(humidity)
        region = category
        
        # For Weather
        category2 = categorize_weather(weather_code)
        weather = category2
        return water_requirement(crop_type,temp,soil_type,region,weather)
    else:
        # Print an error message if the request fails
        return 0

