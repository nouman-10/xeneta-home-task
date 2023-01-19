import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def extract_year_month_date(date):
    return date.split("-")[0], date.split("-")[1], date.split("-")[2]


def calculate_dates_between_two_dates(date_from, date_to):
    year_from, month_from, day_from = extract_year_month_date(date_from)
    year_to, month_to, day_to = extract_year_month_date(date_to)

    dates = []
    while True:
        dates.append(f"{year_from}-{month_from}-{day_from}")
        if f"{year_from}-{month_from}-{day_from}" == f"{year_to}-{month_to}-{day_to}":
            break
        day_from = int(day_from) + 1
        if day_from > 30:
            day_from = 1
            month_from = int(month_from) + 1
            if month_from > 12:
                month_from = 1
                year_from = int(year_from) + 1
    return dates


# Connect to the database

conn = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    port=os.environ.get("DB_PORT"),
)

cursor = conn.cursor()
