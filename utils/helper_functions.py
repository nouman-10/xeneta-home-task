from typing import Dict, List, Tuple

from utils.connect_db import cursor
from utils.sql_queries import PORT_QUERY, PRICE_QUERY, REGION_QUERY


def extract_year_month_date(date: str) -> Tuple[str]:
    return date.split("-")[0], date.split("-")[1], date.split("-")[2]


def calculate_dates_between_two_dates(date_from: str, date_to: str) -> List[str]:
    year_from, month_from, day_from = extract_year_month_date(date_from)
    year_to, month_to, day_to = extract_year_month_date(date_to)

    dates = []
    while True:
        dates.append(f"{year_from:02}-{month_from:02}-{day_from:02}")
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


def find_port_codes(area_slug: str) -> List[str]:
    if len(area_slug) != 5 and not area_slug.isupper():
        cursor.execute(REGION_QUERY.format(parent_slug=area_slug))
        slugs = cursor.fetchall()
        ports = []
        for slug in slugs:
            cursor.execute(PORT_QUERY.format(parent_slug=slug[0]))
            ports.extend([p[0] for p in cursor.fetchall()])
    else:
        ports = [area_slug]
    return ports


def find_prices(origin: str, destination: str, date: str) -> List[int]:
    cursor.execute(
        PRICE_QUERY.format(origin=origin, destination=destination, date=date)
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
