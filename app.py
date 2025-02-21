from flask import Flask, request, render_template # type: ignore
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return render_template("submit.html", city="Unknown", weather_info="City not provided.")

    response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
    
    if response.status_code == 200:
        weather_info = response.text
    else:
        weather_info = "Could not fetch weather data. Try again!"

    return render_template("submit.html", city=city, weather_info=weather_info)

if __name__ == "__main__":
    app.run(debug=True)
