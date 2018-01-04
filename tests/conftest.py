import pytest

from buscaimoveis.app import create_app


@pytest.fixture
def app():
    return create_app('buscaimoveis')
