from flask import Flask, jsonify, request
from connect_db import cursor


app = Flask(__name__)

def extract_year_month_date(date):
    return date.split('-')[0], date.split('-')[1], date.split('-')[2]


def calculate_dates_between_two_dates(date_from, date_to):
    year_from, month_from, day_from = extract_year_month_date(date_from)
    year_to, month_to, day_to = extract_year_month_date(date_to)

    dates = []
    while True:
        dates.append(f'{year_from:02}-{month_from:02}-{day_from:02}')
        if f'{year_from}-{month_from}-{day_from}' == f'{year_to}-{month_to}-{day_to}':
            break
        day_from = int(day_from) + 1
        if day_from > 30:
            day_from = 1
            month_from = int(month_from) + 1
            if month_from > 12:
                month_from = 1
                year_from = int(year_from) + 1
    return dates

region_find_query = "SELECT slug FROM public.regions WHERE parent_slug = '{parent_slug}'"
port_find_query = "SELECT code FROM public.ports WHERE parent_slug = '{parent_slug}'"

price_find_query = "SELECT price FROM public.prices WHERE orig_code = '{origin}' AND dest_code = '{destination}' AND day = '{date}'"


@app.route("/rates")
def calculate_rates():
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    dates = calculate_dates_between_two_dates(date_from, date_to)

    origins = []
    if len(origin) != 5 and not origin.isupper():
        cursor.execute(region_find_query.format(parent_slug=origin))
        slugs = cursor.fetchall()
        for slug in slugs:
            cursor.execute(port_find_query.format(parent_slug=slug[0]))
            ports = cursor.fetchall()
            origins.extend([p[0] for p in ports])
    else:
        origins.append(origin)

    destinations = []
    if len(destination) != 5 and not destination.isupper():
        cursor.execute(region_find_query.format(parent_slug=destination))
        slugs = cursor.fetchall()
        for slug in slugs:
            cursor.execute(port_find_query.format(parent_slug=slug[0]))
            ports = cursor.fetchall()
            destinations.extend([p[0] for p in ports])
    else:
        destinations.append(destination)

    average_prices = {}
    for orig_code in origins:
        for dest_code in destinations:
            for date in dates:
                cursor.execute(price_find_query.format(origin=orig_code, destination=dest_code, date=date))
                prices = cursor.fetchall()
                if date not in average_prices:
                    average_prices[date] = [p[0] for p in prices]
                else:
                    average_prices[date].extend([p[0] for p in prices])

    for date in average_prices:
        if len(average_prices[date]) < 3:
            average_prices[date] = None
        else:
            average_prices[date] = int(sum(average_prices[date]) / len(average_prices[date]))

    avg_prices = [
        {
            'day': date,
            'average_price': average_prices[date]
        } for date in average_prices
    ]
    return jsonify(avg_prices)

    

if __name__ == '__main__':
    app.run(debug=True)
