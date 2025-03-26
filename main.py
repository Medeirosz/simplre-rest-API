from flask import Flask, make_response, jsonify, request
from banco_de_dados import Users

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/users', methods=['GET'])
def get_usuarios():
    return make_response (
        jsonify (
            message = "Lista de usuarios",
            data = Users
        )
    )


@app.route('/users', methods=['POST'])
def create_user(): 
    user = request.json
    Users.append(user)
    return make_response (
        jsonify (
            message = "Carro cadastrado com sucesso.",
            data = Users
        )
    )


app.run()

