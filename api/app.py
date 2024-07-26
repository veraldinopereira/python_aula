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

@app.route('/api/usuarios/cadastrar', methods=['POST'])
def cadastrar():
    new_user = request.get_json()
    with open ('data.json', encoding='utf-8') as file:
        data = json.load(file)

    for element in data['usuarios']:
        if element['email'] == new_user['email']:
            return jsonify({"msg":"email ja cadastrado"})
        if element['nome'] == new_user['nome']:
            return jsonify({"msg": "nome ja cadastrado"})

    new_user['id'] = len(data['usuarios'])+1    
    data['usuarios'].append(new_user)    
    
    with open ('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return jsonify({"msg":"usuario cadastrado com sucesso"})    

@app.route("/api/usuarios/<int:id>", methods=["Put"])
def update_user(id):
    update_data = request.get_json()
    with open("data.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    for element in data['usuarios']:
        if element['id'] == id:
            element.update(update_data)
            with open('data.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file)
            return jsonify({'message': 'Usuario atualizado com sussa'})
    return jsonify({'message': 'Usuario not found'}), 404   

@app.route("/api/usuarios/apagar/<int:id>", methods=['DELETE'])
def delete_user(id):
    with open('data.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    for element in data['usuarios']:
        if element['id'] == id:
            data['usuarios'].remove(element)
            with open('data.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file)
            return jsonify({'message':'usuario deletado com sussa'})
    return jsonify({'message': 'usuario not foun'}), 404

        
if __name__ == '__main__':
    app.run(debug=True)