from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# API requests for weather and cities
api_key = "e35a3b728a550599387fef9ebdd3ff21"
country_reponse = requests.get("https://restcountries.com/v3.1/all?fields=name,flags,capital")

# Retrieving data for the current country. 
# FUTURE IDEA: this api provides the continent for which the country is from, so I can make the multiple choice easier/harder
# based on choosing how many options are from the same continent
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

# Fetching data from the weather API for the current city's weather
current_weather = {
    "temp": "",
    "humidity": "",
    "sky": "",
    "timezone": "",
    #"name": ""
}



def get_weather():
    gen_city()

    if current_country["capital"] != "":
        weather_response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={current_country['capital']}&units=metric&APPID={api_key}")
    else:
        return("Error fetching weather data due to no capital city.")
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
    else:
        return("Error fetching weather data due to invalid status code.")

    current_weather["temp"] = weather_data["main"]["temp"]
    current_weather["humidity"] = weather_data["main"]["humidity"]
    current_weather["sky"] = weather_data["weather"][0]["description"]
    current_weather["timezone"] = weather_data["timezone"]
    #current_weather["name"] = weather_data["name"]


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