# menu.py
#this file contains menu and connects all functions
from weather_api import fetch_weather
from view import view_weather

def menu() -> None:
    """Simple text menu for the user."""
    while True:
        print("===== Weather Map Application =====")
        print("1. Get Weather by City")
        print("2. Get Weather for multiple cities")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()
            if not city:
                print("Please enter a city name.")
                continue
            weather = fetch_weather(city)
            view_weather(weather)

        elif choice == "2":
            cities_line = input("Enter cities separated by commas: ").strip()
            cities = [c.strip() for c in cities_line.split(",") if c.strip()]
            if not cities:
                print("No cities entered.")
                continue
            for c in cities:
                print("-" * 28)
                view_weather(get_weather(c))

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
