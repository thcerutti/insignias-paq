from datetime import datetime
from flask import Flask
from flask_cors import CORS
from models.educando import Educando
from models.insignia import Insignia
from models.nivel_insignia import Nivel_insignia
from flask import request

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return {
        "message": "Hello, World!"
    }, 200

@app.route("/educandos", methods=["GET"])
def get_educandos():
    return {
        "data": [educando.to_json() for educando in Educando.listar_educandos()]
    }, 200

@app.route("/insignias", methods=["GET"])
def get_insignias():
    return {
        "data": [insignia.to_json() for insignia in Insignia.listar_insignias()]
    }, 200

@app.route("/educando/<int:id>/insignias", methods=["GET"])
def get_insiginias_educando(id):
    return {
        "data": [insignia.to_json() for insignia in Educando.listar_insignias(id)]
    }, 200

@app.route("/insignias/<int:id>/requisitos", methods=["GET"])
def get_requisitos(id):
    return {
        "data": Insignia.listar_insignia_por_id(id)
    }, 200

@app.route("/educando/conquista", methods=["POST"])
def post_conquista_insignia():
    # Exemplo de payload:
    # ```json
    # {
    #     "educando_id": 1,
    #     "insignia_id": 1,
    #     "nivel_insignia": 3,
    #     "data_conquista": "2024-11-13"
    # }
    # ```
    data = request.get_json()
    educando = Educando.carregar_educando(data["educando_id"])
    insignia = Insignia.carregar_insignia(data["insignia_id"])
    return {
        "data": {
            "status": "success",
            "educando_id": data["educando_id"],
            "educando_nome": educando.nome_completo,
            "insignia_id": data["insignia_id"],
            "insignia_nome": insignia.nome,
            "nivel_insignia": data["nivel_insignia"],
            "data_conquista": data["data_conquista"],
            "data_registro": datetime.now().isoformat()
        }
    }, 201
