from __future__ import annotations

import pytest
from app import create_app

from tests.functional.db_set_up import db_set_up, db_tear_down


@pytest.fixture()
def app():
    db_set_up()
    app = create_app(testing=True)
    yield app
    db_tear_down()


@pytest.fixture()
def client(app):
    return app.test_client()
