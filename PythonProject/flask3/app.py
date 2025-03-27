#Вариант 14
#Реализуйте маршрут /search, который принимает GET-параметр query и выводит результаты поиска.
from flask import Flask, request, jsonify

app = Flask(__name__)

DATA = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"},
    {"id": 3, "name": "Orange"},
    {"id": 4, "name": "Grape"}
]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    filtered_results = [
        item for item in DATA 
        if query.lower() in item["name"].lower()
    ]
    return jsonify(filtered_results)

if __name__ == '__main__':
    app.run(debug=True)
