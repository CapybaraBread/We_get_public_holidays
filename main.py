from dotenv import load_dotenv
import os
import requests
from datetime import datetime

HOLIDAY_API_URL = "https://calendarific.com/api/v2"

MONTHS_RU_GEN = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]




def get_holidays(api_key, country, year):
    params={
        "api_key": api_key,
        "country": country,
        "year": year
    }
    response = requests.get(f"{HOLIDAY_API_URL}/holidays", params=params)
    return response.json()


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    holidays = get_holidays(api_key, "US", 2025)
    for holiday in holidays.get("response", {}).get("holidays", []):
        month_index = holiday['date']['datetime']['month'] - 1
        month_name = MONTHS_RU_GEN[month_index]
        print(f"{holiday['name']} - {holiday['date']['datetime']['day']} {month_name}")
        print(f"Описание: {holiday['description']}")
        print("")

        
if __name__ == "__main__":
    main()
