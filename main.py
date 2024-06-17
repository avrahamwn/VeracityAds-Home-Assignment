from flask import Flask, request, abort

def create_app():
    return Flask(__name__)

app = create_app()

recipes_dict={}
recipes_ids_counter=0

@app.post("/recipes")
def create_recipe():
    global recipes_ids_counter
    recipe=request.get_json()
    recipes_ids_counter+=1
    recipes_dict[recipes_ids_counter]=recipe
    return recipe

@app.get('/recipes')
def gat_all_recipes():
    return recipes_dict

@app.get('/recipes/<int:id>')
def get_single_recipe(id: int):
    try:
        return recipes_dict[id]
    except KeyError as e:
        abort(404, description="The requested recipe was not found")

@app.put('/recipes/<int:id>')
def update_single_recipe(id: int):
    try:
        recipe = request.get_json()
        recipes_dict[id]=recipe
    except KeyError as e:
        abort(404, description="The requested recipe was not found")
    return recipe

@app.delete('/recipes/<int:id>')
def delete_single_recipe(id:int):
    try:
        del recipes_dict[id]
    except KeyError as e:
        abort(404, description="The requested recipe was not found")
    return f"{id}"


@app.get('/recipes/search')
def search_recipe_by_title_or_category():
    query=request.args.to_dict()
    search_term=query['q']
    filtered_dict=[v for k,v in recipes_dict.items() if (v["title"]==search_term or v["category"]==search_term)]
    return filtered_dict
