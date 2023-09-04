from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# API requests for weather and cities
api_key = "e35a3b728a550599387fef9ebdd3ff21"
country_reponse = requests.get("https://restcountries.com/v3.1/all?fields=name,flags,capital")

# Retrieving data for the current country
current_country = {      #stores the data of the random country obtained. Will be updated with the country's info.
    "name": "",
    "flag": "",
    "capital": ""
}

def gen_city(): 
    if country_reponse.status_code == 200:
        data = country_reponse.json()
    else:
        return("Error: Failed to fetch from country API")

    random_country = random.choice(data)
    country_name = random_country.get("name", {}).get("common","")
    flag_url = random_country.get("flags", {}).get("png", "")
    capital_name = random_country.get("capital", "")[0]

    if country_name:
        current_country["name"] = country_name
    else:
        current_country["name"] = ""
    if flag_url:
        current_country["flag"] = flag_url
    else:
        current_country["flag"] = ""
    if capital_name:
        current_country["capital"] = capital_name
    else: 
        current_country["capital"] = ""


def get_weather():
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q=Houston&units=imperial&APPID={api_key}")
    if weather_data.status_code == 200:
        print(weather_data.json())
    else:
        print("nooo")

get_weather()

"""
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/play")
def play():
    return render_template('play.html')


if __name__ == "__main__":
    app.run(debug=True)

"""