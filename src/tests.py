import pytest
from api import API
from mock_db import MockDB

# fixtures for testing 
@pytest.fixture
def mock_db():
    return MockDB()

# test case to assert that the API returns the correct prizes for a valid catalog_id
def test_list_prizes_with_valid_catalog_id(mock_db):
    api = API(mock_db)
    catalog_id = 1
    assert len(api.list_prizes(catalog_id)) > 0

# test case to assert that the API returns None for an invalid catalog_id
def test_list_prizes_with_invalid_catalog_id(mock_db):
    api = API(mock_db)
    catalog_id = 100  # invalid catalog_id (not present in the mock database)
    assert api.list_prizes(catalog_id) == None


# test case to assert that the API returns the correct prizes for a valid catalog_id and filter
def test_list_prizes_with_valid_catalog_id_and_filter(mock_db):
    api = API(mock_db)
    catalog_id = 1
    filter = {"category": "Electronics"}
    assert len(api.list_prizes(catalog_id, filter)) > 0

# test case to assert the API returns the correct number of prizes for a given "per_page" number
def test_list_prizes_with_per_page(mock_db):
    import json
    api = API(mock_db)
    catalog_id = 1
    per_page = 5
    pagination_params = {"per_page": per_page}
    prizes = api.list_prizes(catalog_id, pagination=pagination_params)
    assert len(json.loads(prizes)["prizes"]) == per_page

# test case to assert the API returns the correct number of prizes for a given "page" number
def test_list_prizes_with_page(mock_db):
    import json
    api = API(mock_db)
    catalog_id = 1
    page = 2
    per_page = 2 # small number according to mock data
    pagination_params = {"page": page, "per_page": per_page}
    prizes = api.list_prizes(catalog_id, pagination=pagination_params)
    assert len(json.loads(prizes)["prizes"]) == per_page