from flask import Flask, render_template
import requests

app = Flask(__name__)

# API requests for weather and cities
api_key = "e35a3b728a550599387fef9ebdd3ff21"
country_reponse = requests.get("https://restcountries.com/v3.1/all?fields=name,flags,capital")

if country_reponse.status_code == 200:
    data = country_reponse.json()
    print(data)

def gen_city(): 
    exit


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/play")
def play():
    return render_template('play.html')


if __name__ == "__main__":
    app.run(debug=True)


