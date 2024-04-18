from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


def connection():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="1234", database="pacientes"
    )
    return conn


@app.route("/pacientes", methods=["GET"])
def get_all():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM paciente")
    pacientes = cursor.fetchall()

    conn.close()

    keys = []
    for i in cursor.description:
        keys.append(i[0])

    data = []
    for paciente in pacientes:
        dicts = dict(zip(keys, paciente))
        data.append(dicts)

    return jsonify(data)


# Rota para criar um novo paciente
@app.route("/pacientes", methods=["POST"])
def create_paciente():
    conn = connection()
    cursor = conn.cursor()

    data = request.get_json()
    print("Data received:", data)  # Adicione esta linha para depurar

    nome = data.get("nome")
    idade = data.get("idade")
    sexo = data.get("sexo")
    cidade = data.get("cidade")

    if nome and idade and sexo and cidade:
        cursor.execute(
            "INSERT INTO paciente (nome, idade, sexo, cidade) VALUES (%s, %s, %s, %s)",
            (nome, idade, sexo, cidade),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Paciente criado com sucesso"}), 201
    else:
        conn.close()
        return jsonify({"message": "Campos obrigatórios não fornecidos"}), 400


# Rota para buscar por ID
@app.route("/pacientes/<int:id>", methods=["GET"])
def get_by_id(id):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM paciente WHERE id = %s", (id,))
    paciente = cursor.fetchone()

    conn.close()

    if paciente:
        keys = [i[0] for i in cursor.description]
        data = dict(zip(keys, paciente))
        return jsonify(data)
    else:
        return jsonify({"message": "Paciente não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
