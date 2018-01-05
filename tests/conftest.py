import pytest

from mongomock import MongoClient

from buscaimoveis.app import create_app
from tests.fixtures import ads_fixture_data


@pytest.fixture
def app():
    app = create_app('buscaimoveis')
    app.db = MongoClient().db

    ads_fixture_data(app.db)

    return app
