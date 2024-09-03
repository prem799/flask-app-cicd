import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Create an Item" in response.data

def test_create_item(client):
    response = client.post('/create', data={'name': 'Test Item', 'description': 'This is a test'})
    assert response.status_code == 200
    assert b"Item Created Successfully!" in response.data

def test_items_page(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert b"Items" in response.data

def test_items_page_with_items(client):
    client.post('/create', data={'name': 'Test Item', 'description': 'This is a test'})
    response = client.get('/items')
    assert response.status_code == 200
    assert b"Test Item" in response.data
    assert b"This is a test" in response.data

def test_invalid_route(client):
    response = client.get('/invalid')
    assert response.status_code == 404