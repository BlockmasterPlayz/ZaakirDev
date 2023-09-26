from flask import Flask, render_template, request
import requests

app = Flask(__name__)
CurrentWeather = ""
APIkey = "37eba855051da40658c9cc512164d698"
lat = ""
lon = ""



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods=["POST"])
def input():
    lat = request.form.get("Lat")
    lon = request.form.get("Lon")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}"

    response = requests.get(url)
    data = response.json()

    CurrentWeather = data["weather"][0]["description"]
    return render_template("Weather.html", Current_Weather = CurrentWeather)


if __name__ == "__main__":
    app.run(debug=True)
