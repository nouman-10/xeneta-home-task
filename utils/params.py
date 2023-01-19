from enum import Enum


class Param(Enum):
    """Enum class for parameters"""

    DATE_FROM = 1
    DATE_TO = 2
    ORIGIN = 3
    DESTINATION = 4


ParamConfig = {
    "date_from": Param.DATE_FROM,
    "date_to": Param.DATE_TO,
    "origin": Param.ORIGIN,
    "destination": Param.DESTINATION,
}
