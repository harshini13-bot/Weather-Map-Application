# weather_api.py
import requests

API_URL = "http://api.openweathermap.org/data/2.5/weather"

# === Put your permanent API key here (replace the placeholder) ===
API_KEY = "04518ade466e53ed7aa204607fcf177f"

def fetch_weather(city: str) -> dict:
    """Fetch weather for a city from OpenWeatherMap."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        r = requests.get(API_URL, params=params, timeout=10)
        data = r.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
    except ValueError:
        return {"error": "Invalid response from the weather service."}

    if r.status_code != 200:
        return {"error": data.get("message", f"API returned status {r.status_code}")}

    main = data.get("main", {})
    weather_list = data.get("weather", [{}])
    description = weather_list[0].get("description", "No description").capitalize()

    return {
        "city": data.get("name", city),
        "temperature": main.get("temp"),
        "humidity": main.get("humidity"),
        "description": description
    }
