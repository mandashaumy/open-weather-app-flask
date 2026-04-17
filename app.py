import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("OPENWEATHER_API_KEY")
is_debug = os.getenv("DEBUG")

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            # OpenWeatherMap API URL
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
            response = requests.get(url)
            
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = "City not found or API error. Please try again."

    return render_template('index.html', weather=weather_data, error=error_message)

@app.route('/loaderio-2a09fd170d346b1cef29707f05afb011.txt')
@app.route('/loaderio-2a09fd170d346b1cef29707f05afb011.html')
@app.route('/loaderio-2a09fd170d346b1cef29707f05afb011/')
def loaderio():
    return "loaderio-2a09fd170d346b1cef29707f05afb011"

if __name__ == '__main__':
    # Convert the DEBUG environment variable to a boolean for Flask
    debug_mode = str(is_debug).lower() in ("true", "1", "t")
    app.run(debug=debug_mode)