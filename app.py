from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# API requests for weather and cities
api_key = "e35a3b728a550599387fef9ebdd3ff21"
country_reponse = requests.get("https://restcountries.com/v3.1/all?fields=name,flags,capital")


def gen_city(): 
    if country_reponse.status_code == 200:
        data = country_reponse.json()
    else:
        return("Error: Failed to fetch from country API")

    random_country = random.choice(data)
    country_name = random_country.get("name", {}).get("common","")
    flag_url = random_country.get("flags", {}).get("png", "")
    capital_name = random_country.get("capital", "")

    if country_name:
        print(country_name)
    else:
        print("oops")
    if flag_url:
        print(flag_url)
    else:
        print("no flag")
    if capital_name:
        print(capital_name)
    else: 
        print("no capital")

gen_city()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/play")
def play():
    return render_template('play.html')


if __name__ == "__main__":
    app.run(debug=True)

