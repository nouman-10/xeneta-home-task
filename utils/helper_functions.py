from datetime import datetime, timedelta
import os
from typing import Dict, List

from utils.connect_db import cursor
from utils.sql_queries import PORT_QUERY, PRICE_QUERY, REGION_QUERY


IS_TESTING = os.environ.get("TESTING", False)


def calculate_dates_between_two_dates(date_from: str, date_to: str) -> List[str]:
    date_from_dt = datetime.strptime(date_from, "%Y-%m-%d")
    date_to_dt = datetime.strptime(date_to, "%Y-%m-%d")

    dates = []
    while True:
        dates.append(
            f"{date_from_dt.year}-{date_from_dt.month:02}-{date_from_dt.day:02}"
        )
        if date_from_dt == date_to_dt:
            break
        date_from_dt += timedelta(days=1)
    return dates


def find_port_codes(area_slug: str) -> List[str]:
    if len(area_slug) != 5 and not area_slug.isupper():
        cursor.execute(REGION_QUERY, (area_slug,))
        slugs = cursor.fetchall()
        ports = []
        slugs = [s[0] for s in slugs] if slugs else [area_slug]
        for slug in slugs:
            cursor.execute(PORT_QUERY, (slug,))
            ports.extend([p[0] for p in cursor.fetchall()])
    else:
        ports = [area_slug]

    return ports


def find_prices(origin: str, destination: str, date: str) -> List[int]:
    cursor.execute(
        PRICE_QUERY,
        (
            origin,
            destination,
            date,
        ),
    )
    prices = cursor.fetchall()
    return [p[0] for p in prices]


def calculate_avg_price(prices: List[int]) -> int or None:
    if len(prices) < 3:
        return None
    else:
        return int(sum(prices) / len(prices))


def format_data(prices: Dict[str, List[int]]) -> List[Dict[str, int or None]]:
    return [
        {"day": date, "average_price": calculate_avg_price(prices[date])}
        for date in prices
    ]
