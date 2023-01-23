from flask import Blueprint, jsonify

import utils.helper_functions as f
from utils.validate_input import RequestData, validate_input, validate_date_range

rates_api = Blueprint("api", __name__)


@rates_api.route("/")
def calculate_rates():
    request_data = RequestData.from_request()
    errors = validate_input(request_data)
    if errors:
        return jsonify({"errors": errors}), 400

    date_from = request_data.date_from
    date_to = request_data.date_to
    origin = request_data.origin
    destination = request_data.destination

    is_valid_range = validate_date_range(date_to, date_from)
    if not is_valid_range:
        return jsonify({"Error": "date_from should be equal or less than date_to"}), 400

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
