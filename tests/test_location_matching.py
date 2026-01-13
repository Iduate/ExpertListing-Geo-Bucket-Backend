import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Test case: All Sangotedo variants should return all 3 properties
@pytest.mark.parametrize("search_term", ["Sangotedo", "sangotedo lagos", "Sangotedo, Ajah"])
def test_search_sangotedo_variants(search_term):
    response = client.get(f"/api/properties/search?location={search_term}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    locations = [prop["location_name"].lower() for prop in data]
    assert any("sangotedo" in loc for loc in locations)

# Test case: Typo tolerance
@pytest.mark.parametrize("search_term", ["Sangotedoo", "Sangoted", "Sangotedo"])
def test_search_typo_tolerance(search_term):
    response = client.get(f"/api/properties/search?location={search_term}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3

# Test case: Case insensitivity
@pytest.mark.parametrize("search_term", ["SANGOTEDO", "sAngOtEdO"])
def test_search_case_insensitivity(search_term):
    response = client.get(f"/api/properties/search?location={search_term}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
