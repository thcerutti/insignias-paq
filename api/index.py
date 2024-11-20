from datetime import datetime
from flask import request
from flask import Flask, jsonify
from flask_cors import CORS
from models.insignia import Insignia
from models.educando import Educando

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return {
        "message": "Hello, World!"
    }, 200

@app.route("/educandos", methods=["GET"])
def get_educandos():
    educandos = [educando.to_json() for educando in Educando.Listar_educandos()]
    if not educandos:
        return {"error": "Educandos não encontrados."}, 404
    return educandos, 200

@app.route("/insignias", methods=["GET"])
def get_insignias():
    insignias = [insignia.to_json() for insignia in Insignia.listar_insignias()]
    if not insignias:
        return {"error": "Insignias não encontradas."}, 404
    return insignias, 200

@app.route("/educando/<int:id>", methods=["GET"])
def get_educando(id):
    educando = Educando.carregar_educando(id)
    if not educando:
        return {"error": "Educando não encontrado."}, 404
    return educando.to_json(), 200

@app.route("/educando/<int:id>/insignias", methods=["GET"])
def get_insiginias_educando(id):
    insigniasDoEducando = [insignia for insignia in Educando.carregar_educando(id).insignias]
    if not insigniasDoEducando:
        return {"error": "Educando não encontrado."}, 404
    return insigniasDoEducando, 200

@app.route("/insignia/<int:id>", methods=["GET"])
def get_requisitos(id):
    insignia = Insignia.carregar_insignia(id)
    if not insignia:
        return {"error": "Insignia não encontrada."}, 404

    return insignia, 200

@app.route("/educando/conquista", methods=["POST"])
def post_conquista_insignia():
    if not request.is_json:
        return {"Erro, conteudo deve ser um content-type/json"}, 415

    data = request.get_json()
    educando = Educando.carregar_educando(data["educando_id"])
    insignia = Insignia.carregar_insignia(data["insignia_id"])

    return {
        "status": "success",
        "educando_id": data["educando_id"],
        "educando_nome": educando.nome,
        "insignia_id": data["insignia_id"],
        "insignia_nome": insignia.nome,
        "nivel_insignia": data["nivel_insignia"],
        "data_conquista": data["data_conquista"],
        "data_registro": datetime.now().isoformat()
    }, 201

@app.route("/insignias/criar", methods=["POST"])
def post_criar_insiginia():
    data = request.get_json()
    insignia = Insignia(data.get("id"),data.get("nome"),data.get("trilha"),data.get("niveis"))
    mensagem = insignia.gravar_insignia()

    return {
        "status": "success",
        "message": mensagem
        #"data": data
    }, 201
