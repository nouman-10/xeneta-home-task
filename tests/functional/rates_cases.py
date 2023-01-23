from utils.validate_input import invalid_messages
from utils.params import Param

correct_responses = [
    [
        {"day": "2020-01-01", "average_price": 100},
        {"day": "2020-01-02", "average_price": None},
        {"day": "2020-01-03", "average_price": 190},
        {"day": "2020-01-04", "average_price": None},
    ],
    [
        {"day": "2020-01-01", "average_price": 100},
        {"day": "2020-01-02", "average_price": None},
    ],
    [
        {"day": "2020-01-03", "average_price": 190},
        {"day": "2020-01-04", "average_price": None},
    ],
]


correct_params = [
    {
        "date_from": "2020-01-01",
        "date_to": "2020-01-04",
        "origin": "north_europe_sub",
        "destination": "china_main",
    },
    {
        "date_from": "2020-01-01",
        "date_to": "2020-01-02",
        "origin": "north_europe_sub",
        "destination": "CNCWN",
    },
    {
        "date_from": "2020-01-03",
        "date_to": "2020-01-04",
        "origin": "IESNN",
        "destination": "CNCWN",
    },
]

missing_params = {
    invalid_messages[Param.DATE_FROM]: {
        "date_to": "2020-01-04",
        "origin": "north_europe_sub",
        "destination": "china_main",
    },
    invalid_messages[Param.DATE_TO]: {
        "date_from": "2020-01-01",
        "origin": "north_europe_sub",
        "destination": "CNCWN",
    },
    invalid_messages[Param.ORIGIN]: {
        "date_from": "2020-01-03",
        "date_to": "2020-01-04",
        "destination": "CNCWN",
    },
    invalid_messages[Param.DESTINATION]: {
        "date_from": "2020-01-03",
        "date_to": "2020-01-04",
        "origin": "CNCWN",
    },
}


invalid_params = {
    invalid_messages[Param.DATE_FROM]: {
        "date_from": "2020-30-01",
        "date_to": "2020-01-04",
        "origin": "north_europe_sub",
        "destination": "china_main",
    },
    invalid_messages[Param.ORIGIN]: {
        "date_from": "2020-01-01",
        "date_to": "2020-01-02",
        "origin": 234,
        "destination": "CNCWN",
    },
    "date_from should be equal or less than date_to": {
        "date_from": "2020-01-05",
        "date_to": "2020-01-04",
        "origin": "IESNN",
        "destination": "CNCWN",
    },
}
