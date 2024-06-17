import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_recipe(client):
    response = client.post('/recipes', json={ "title": "Test Recipe", "description": "A classic Italian pasta dish with a creamy egg sauce.", "ingredients": [ "200g spaghetti", "100g pancetta", "2 large eggs", "50g grated Parmesan cheese", "Salt", "Black pepper" ], "instructions": "...", "category": "Pasta" })
    assert response.status_code == 200
    assert response.json['title'] == 'Test Recipe'

def test_get_all_recipes(client):
    response = client.get('/recipes')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_get_single_recipe(client):
    # Assuming there is already a recipe with ID 1
    response = client.get('/recipes/1')
    assert response.status_code == 200
    assert 'title' in response.json

def test_update_single_recipe(client):
    # Assuming there is already a recipe with ID 1
    response = client.put('/recipes/1', json={ "title": "Updated Test Recipe", "description": "A classic Italian pasta dish with a creamy egg sauce.", "ingredients": [ "200g spaghetti", "100g pancetta", "2 large eggs", "50g grated Parmesan cheese", "Salt", "Black pepper" ], "instructions": "...", "category": "Updated Test Category" })
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Test Recipe'

def test_search_recipe_by_title_or_category(client):
    # Assuming there is already a recipe with title 'Test Recipe'
    response = client.get('/recipes/search?q=Updated Test Recipe')
    print(response.json)
    assert response.status_code == 200
    assert any(recipe['title'] == 'Updated Test Recipe' for recipe in response.json)

def test_delete_single_recipe(client):
    # Assuming there is already a recipe with ID 1
    response = client.delete('/recipes/1')
    assert response.status_code == 200


