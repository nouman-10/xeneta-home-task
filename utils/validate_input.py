from typing import List
from dataclasses import dataclass
from datetime import datetime

from flask import request

from utils.params import Param, ParamConfig
from utils.connect_db import cursor
from utils.sql_queries import PORT_CODES_QUERY, REGION_NAMES_QUERY


cursor.execute(PORT_CODES_QUERY)

PORT_CODES = [p[0] for p in cursor.fetchall()]

cursor.execute(REGION_NAMES_QUERY)
REGIONS = [r[0] for r in cursor.fetchall()]


@dataclass(frozen=True)
class Request:
    date_from: str
    date_to: str
    origin: str
    destination: str

    @classmethod
    def from_request(cls):
        return cls(
            date_from=request.args.get("date_from"),
            date_to=request.args.get("date_to"),
            origin=request.args.get("origin"),
            destination=request.args.get("destination"),
        )


def validate_date(date: str) -> bool:
    """Validate date format"""
    if date is None:
        return False
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_area(area: str) -> bool:
    """Validate area format"""
    if area is None:
        return False
    return area in PORT_CODES or area in REGIONS


value_validator = {
    Param.DATE_FROM: validate_date,
    Param.DATE_TO: validate_date,
    Param.ORIGIN: validate_area,
    Param.DESTINATION: validate_area,
}


invalid_messages = {
    Param.DATE_FROM: "date_from is required and the correct format is YYYY-MM-DD",
    Param.DATE_TO: "date_to is required and the correct format YYYY-MM-DD",
    Param.ORIGIN: "origin is required and should be either 5 digit port code or a valid region name",
    Param.DESTINATION: "destination is required and should be either 5 digit port code or a valid region name",
}


def validate_input(request: Request) -> List[str]:
    """Validate input parameters"""
    errors = []
    for param in ParamConfig:
        if not value_validator[ParamConfig[param]](getattr(request, param)):
            errors.append(invalid_messages[ParamConfig[param]])
    return errors


def validate_date_range(date_to: str, date_from: str) -> bool:
    """Validate date range"""
    return datetime.strptime(date_to, "%Y-%m-%d") >= datetime.strptime(
        date_from, "%Y-%m-%d"
    )
