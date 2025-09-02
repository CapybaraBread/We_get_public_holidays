from dotenv import load_dotenv
import os
import requests

HOLIDAY_API_URL = "https://calendarific.com/api/v2"

def get_holidays(api_key, country, year):
    response = requests.get(f"{HOLIDAY_API_URL}/holidays", params={
        "api_key": api_key,
        "country": country,
        "year": year
    })
    return response.json()

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    holidays = get_holidays(api_key, "US", 2025)
    for holiday in holidays.get("response", {}).get("holidays", []):
        print(f"{holiday['name']} в {holiday['date']['iso']}")
        print(f"Описание: {holiday['description']}")
if __name__ == "__main__":
    main()