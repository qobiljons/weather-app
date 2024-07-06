# Weather Comparison App

This Django web application allows users to compare weather data for two cities.

## Features

* **City Comparison:** Compare current weather and 5-day forecasts.
* **Weather Data:** Displays temperature, description, and icons.
* **Responsive Design:** Built with Bootstrap for a user-friendly experience.
* **API Integration:** Utilizes the OpenWeatherMap API.

## Technologies

* Django: Web framework
* Bootstrap: CSS framework
* OpenWeatherMap API: Weather data provider
* Python: Programming language

## Installation

**Prerequisites:**

* Git
* Python 3 and pip

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd weather-comparison-app

2. **Install Dependencies:**
   ```bash
   pipenv install
   pipenv shell  # Activate virtual environment (optional)

3. **Set Up Environment Variables**
   Create a file named .env in the root directory. Add the following lines, replacing placeholders:
   ```bash
   WEATHER_API_KEY=<your_openweathermap_api_key>
   SECRET_KEY=YOUR_SECRET_KEY   
Get your API key from OpenWeatherMap.

4. **Run the development server**
   ```bash
   python manage.py runserver

5. **Usage**
   Visit http://localhost:8000/ in your browser.
   Enter city names in the form fields.
   Click "Compare Weather".
View weather details and forecasts for both cities.
Note: This is a basic setup guide. Additional configuration and development steps might be required.
