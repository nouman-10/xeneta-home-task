import pytest

from tests.functional.rates_cases import (
    correct_params,
    missing_params,
    correct_responses,
    invalid_params,
)


@pytest.mark.parametrize(
    "parameters, correct_response", zip(correct_params, correct_responses)
)
def test_correct_rates(client, parameters, correct_response):
    response = client.get("/rates/", query_string=parameters)
    assert response.status_code == 200, response.json == correct_response


@pytest.mark.parametrize("parameters, error", missing_params.items())
def test_missing_params(client, parameters, error):
    response = client.get("/rates/", query_string=parameters)
    assert response.status_code == 400, response.json == {"errors": [error]}


@pytest.mark.parametrize("parameters, error", invalid_params.items())
def test_invalid_params(client, parameters, error):
    response = client.get("/rates/", query_string=parameters)
    assert response.status_code == 400, response.json == {"errors": [error]}
