from flask import Blueprint, jsonify, request

import utils.helper_functions as f

rates_api = Blueprint("api", __name__)


@rates_api.route("/")
def calculate_rates():
    date_from = request.args.get("date_from")
    date_to = request.args.get("date_to")
    origin = request.args.get("origin")
    destination = request.args.get("destination")

    dates = f.calculate_dates_between_two_dates(date_from, date_to)

    orig_codes = f.find_port_codes(origin)
    dest_codes = f.find_port_codes(destination)

    all_prices = {}
    for orig_code in orig_codes:
        for dest_code in dest_codes:
            for date in dates:
                prices = f.find_prices(orig_code, dest_code, date)
                if date not in all_prices:
                    all_prices[date] = prices
                else:
                    all_prices[date].extend(prices)

    avg_prices = f.format_data(all_prices)
    return jsonify(avg_prices)
