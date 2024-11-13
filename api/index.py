from flask import Flask
from flask_cors import CORS
from models.educando import Educando
from models.insignia import Insignia
from models.nivel_insignia import Nivel_insignia

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
    return{
        "data":{
            "status": "success"
        }
    }
