# from flask import Flask, jsonify
# import json

# app = Flask(__name__)

# # Load recipes from the JSON file
# def load_recipes():
#     try:
#         with open('recipes.json', 'r') as f:
#             content = f.read()
#             print(f"Content of recipes.json: '{content}'")  # Print the content
#             data = json.loads(content)
#             return data['recipes']
#     except FileNotFoundError as e:
#         print(f"Error loading recipes: {e}")
#         return []
#     except json.JSONDecodeError as e:
#         print(f"JSON Decode Error: {e}")
#         return []
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return []

# recipes = load_recipes()

# # Endpoint to get a list of all recipe names and IDs
# @app.route('/recipes', methods=['GET'])
# def get_all_recipes():
#     recipe_list = [{'id': recipe['id'], 'name': recipe['name']} for recipe in recipes]
#     return jsonify(recipes=recipe_list)

# # Endpoint to get details of a specific recipe by ID
# @app.route('/recipes/<int:recipe_id>', methods=['GET'])
# def get_recipe(recipe_id):
#     recipe = next((r for r in recipes if r['id'] == recipe_id), None)
#     if recipe:
#         return jsonify(recipe)
#     return jsonify(({'message': 'Recipe not found'}), 404)

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, jsonify, send_file
import json
import os

app = Flask(__name__)

# Load recipes from the JSON file
def load_recipes():
    try:
        with open('recipes.json', 'r') as f:
            content = f.read()
            print(f"Content of recipes.json: '{content}'")
        data = json.loads(content)
        return data['recipes']
    except FileNotFoundError as e:
        print(f"Error loading recipes: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

recipes = load_recipes()

# Serve the index.html file
@app.route('/', methods=['GET'])
def index():
    return send_file('index.html')  # Assuming index.html is in the same directory

# Endpoint to get a list of all recipe names and IDs
@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    recipe_list = [{'id': recipe['id'], 'name': recipe['name']} for recipe in recipes]
    return jsonify(recipes=recipe_list)

# Endpoint to get details of a specific recipe by ID
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({'message': 'Recipe not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
