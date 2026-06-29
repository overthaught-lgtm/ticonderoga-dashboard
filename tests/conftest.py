"""Pytest configuration and fixtures."""
import pytest
from api.app import create_app


@pytest.fixture
def app():
    """Create and configure a test Flask app."""
    app = create_app({"TESTING": True})
    return app


@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()
