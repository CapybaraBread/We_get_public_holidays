from dotenv import load_dotenv
import os
import requests
from datetime import datetime

HOLIDAY_API_URL = "https://calendarific.com/api/v2"

MONTHS_RU_GEN = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}

def format_date_ru(iso_str: str) -> str:
    date_part = iso_str[:10]
    try:
        dt = datetime.strptime(date_part, "%Y-%m-%d")
        return f"{dt.day} {MONTHS_RU_GEN.get(dt.month, '')}"
    except Exception:
        return iso_str

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
        iso = holiday.get('date', {}).get('iso', '')
        ru_date = format_date_ru(iso) if iso else ""
        print(f"{holiday['name']} {ru_date}")
        print(f"Описание: {holiday['description']}")
        print("")
if __name__ == "__main__":
    main()
