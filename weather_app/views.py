import os
import datetime
import requests
from django.shortcuts import render

def index(request):
    api_key = os.getenv("WEATHER_API_KEY")
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}"
    
    if request.method == "GET":
        return render(request, template_name="weather_app/index.html")
    elif request.method == "POST":
        city1 = request.POST.get('city1', '')
        city2 = request.POST.get('city2', '')

        if city1:
            weather_data1, daily_forecast1 = fetch_weather_data(city1, api_key, current_weather_url, forecast_url)
        else:
            weather_data1, daily_forecast1 = None, None

        if city2:
            weather_data2, daily_forecast2 = fetch_weather_data(city2, api_key, current_weather_url, forecast_url)
        else:
            weather_data2, daily_forecast2 = None, None
        
        context = {
            "weather_data1": weather_data1,
            "daily_forecast1": daily_forecast1,
            "weather_data2": weather_data2,
            "daily_forecast2": daily_forecast2,
        }
        return render(request, template_name="weather_app/index.html", context=context)

def fetch_weather_data(city, api_key, current_weather_url, forecast_url):
    # Fetch current weather data
    current_response = requests.get(current_weather_url.format(city, api_key))
    if current_response.status_code == 200:
        current_data = current_response.json()
        
        # Extract necessary data from current weather response
        weather_data = {
            "city": city,
            "temperature": round(current_data['main']['temp'] - 271.15, 2),
            "description": current_data["weather"][0]["description"],
            "icon": current_data["weather"][0]["icon"],
            "wind_speed": current_data["wind"]["speed"],
            "humidity": current_data["main"]["humidity"],
            "sunrise": datetime.datetime.fromtimestamp(current_data["sys"]["sunrise"]),
        }

        # Fetch forecast data using coordinates from current weather response
        lon = current_data["coord"]["lon"]
        lat = current_data["coord"]["lat"]
        forecast_response = requests.get(forecast_url.format(lat, lon, api_key))
        
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()["list"]
            daily_forecasts = []

            for daily_data in forecast_data:
                daily_forecasts.append({
                    "day": datetime.datetime.fromtimestamp(daily_data["dt"]).strftime("%A"),
                    "min_temp": round(daily_data["main"]["temp_min"] - 271.15, 2),
                    "max_temp": round(daily_data["main"]["temp_max"] - 271.15, 2),
                    "description": daily_data["weather"][0]["description"],

                    "icon": daily_data["weather"][0]["icon"],
                })
        
            
            return weather_data, daily_forecasts
        else:
            print(f"Failed to fetch forecast data for {city}. Status code: {forecast_response.status_code}")
            return None, None

    else:
        print(f"Failed to fetch current weather data for {city}. Status code: {current_response.status_code}")
        return None, None
