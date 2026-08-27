import pytest

from aaa_api import create_app


@pytest.fixture()
def client():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )

    with app.test_client() as test_client:
        yield test_client
