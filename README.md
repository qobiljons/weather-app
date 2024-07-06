# Weather Comparison App

The Weather Comparison App is an online application that allows users to compare the current weather conditions and 5-day forecasts for two cities. Built using Django, Bootstrap, and the OpenWeatherMap API, this app provides a user-friendly interface for quickly accessing and comparing weather data.

## Features

- **City Comparison:** Compare weather data for two cities side-by-side.
- **Current Weather:** Display current temperature, weather description, and weather icon for each city.
- **5-Day Forecast:** View a 5-day forecast including minimum and maximum temperatures, weather descriptions, and icons.
- **Sleek Interface:** Designed with Bootstrap for a modern and responsive layout.
- **API Integration:** Utilizes the OpenWeatherMap API to fetch real-time weather data.

## Technologies Used

- **Django:**
- **Bootstrap:** 
- **OpenWeatherMap API:** 
- **HTML/CSS:** 
- **Python:**

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd weather-comparison-app
   
# Install Dependencies:

2. **Create and activate a virtual environment (optional but recommended)**
 
 ```bash
   pipenv install
   pipenv shell

3. **Set up environment variables**

# Create a .env file in the root directory with the following variables:
# Replace <your_openweathermap_api_key> with your actual OpenWeatherMap API key.

```bash
echo "WEATHER_API_KEY=<your_openweathermap_api_key>" > .env
SECRET_KEY="YOUR_SECRET_KEY"
WEATHER_API_KEY=<your_openweathermap_api_key>


**Run the Development Server**
   python manage.py runserver

#The app will be available at http://localhost:8000.


**Usage**
   # Enter two city names in the provided form fields and click on Compare Weather.
   # The app will display the current weather details and a 5-day forecast for each city.
   # Enjoy comparing weather data between different cities effortlessly!

