# Flask Recipes API

This project is a simple Flask application that provides an API for managing recipes. It allows clients to create, retrieve, update, and delete recipes, as well as search for recipes by title or category.

## Installation

To run this project, you will need Python and Flask installed on your system. If you don't have Flask installed, you can install it using pip:

```bash
pip install Flask
```
## Running the Application
To start the server, add the following env variables:
```chatinput
FLASK_APP=main
FLASK_ENV=development
```
Then run the following command from the root directory of the project:

```bash
flask run
```
The API will be available at http://127.0.0.1:5000/.

## API Endpoints
POST /recipes: Create a new recipe.<br>
GET /recipes: Get all recipes.<br>
GET /recipes/<id>: Get a single recipe by ID.<br>
PUT /recipes/<id>: Update a recipe by ID.<br>
DELETE /recipes/<id>: Delete a recipe by ID.<br>
GET /recipes/search: Search for recipes by title or category.

## Example Requests
<b>Recipe Json Example:</b><br>
`{
   "title": "Spaghetti Carbonara",
   "description": "A classic Italian pasta dish with a creamy egg sauce.",
   "ingredients": [
       "200g spaghetti",
       "100g pancetta",
       "2 large eggs",
       "50g grated Parmesan cheese",
       "Salt",
       "Black pepper"
   ],
   "instructions": "...",
   "category": "Pasta"
}`<br>

<b>Create a Recipe</b><br>
curl -X POST -H "Content-Type: application/json" -d 'YOUR_JSON' http://127.0.0.1:5000/recipes

<b>Get All Recipes</b><br>
curl http://127.0.0.1:5000/recipes

<b>Get Single Recipe</b><br>
curl http://127.0.0.1:5000/recipes/1

<b>Update Single Recipe</b><br>
curl -X PUT -H "Content-Type: application/json" -d 'YOUR_JSON' http://127.0.0.1:5000/recipes/1

<b>Delete Single Recipe</b><br>
curl -X DELETE http://127.0.0.1:5000/recipes/1

<b>Search Recipe by Title or Category</b><br>
curl "http://127.0.0.1:5000/recipes/search?q=Pancakes"

<b>Error Handling</b><br>
The API will return appropriate HTTP status codes for various error scenarios.

## Testing

This project uses ```pytest``` for testing its API endpoints.

To run the tests, ensure you have pytest installed:

```bash
pip install pytest
```

Once installed, you can run the tests using the pytest command in the root directory of the project. 
The test cases are located in the test_app.py file:
```bash
pytest ./test.py
```