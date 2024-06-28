from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/usuarios', methods=['GET'])
def index():
    with open ('data.json', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/api/usuarios/<id>', methods=['GET'])
def buscar_id(id):
    with open ('data.json', encoding='utf-8') as file:
        data = json.load(file)
    for element in data['usuarios']:
        if element['id'] == int(id):
            return jsonify(element)
    return jsonify({'msg':'no existe usuario com esse ID'})

if __name__ == '__main__':
    app.run(debug=True)