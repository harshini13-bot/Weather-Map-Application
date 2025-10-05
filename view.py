# view.py
def view_weather(weather_data: dict) -> None:
    """Print weather info or error to console."""
    if not weather_data:
        print("No weather data to show.")
        return
    if "error" in weather_data:
        print("Error:", weather_data["error"])
        return

    print(f"\nCity: {weather_data['city']}")
    temp = weather_data.get("temperature")
    if temp is not None:
        print(f"Temperature: {temp}°C")
    else:
        print("Temperature: N/A")

    humidity = weather_data.get("humidity")
    print(f"Humidity: {humidity if humidity is not None else 'N/A'}%")
    print(f"Description: {weather_data.get('description', 'N/A')}\n")
