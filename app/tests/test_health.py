"""
Tests for the health endpoints.
"""

import os
import pytest
from fastapi.testclient import TestClient

# Set environment variable to test mode before importing app
os.environ["TESTING"] = "True"

from app.api.app import app


@pytest.fixture
def client():
    """Create a test client for the application."""
    return TestClient(app)


def test_root_endpoint(client):
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "documentation" in response.json()


def test_health_check_endpoint(client):
    """Test the health check endpoint."""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    
    # Check response format
    data = response.json()
    assert "status" in data
    assert "timestamp" in data
    assert "version" in data
    assert "database_connected" in data
    
    # In this test case, database_connected might be False
    # since we're not setting up a test database for the unit test
    # In a more comprehensive integration test, we'd expect it to be True
