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
    return jsonify({
        "data": [educando.to_json() for educando in Educando.Listar_educandos()]
    }), 200
        
@app.route("/insignias", methods=["GET"])
def get_insignias():
    return {
        "data": [insignia.to_json() for insignia in Insignia.listar_insignias()]
    }, 200 
    
@app.route("/educando/<int:id>/insignias", methods=["GET"])
def get_insiginias_educando(id):   
    return {
        "data": [insignia for insignia in Educando.carregar_educando(id).insignias]
    }, 200

@app.route("/insignias/<int:id>/requisitos", methods=["GET"])
def get_requisitos(id):
    return {
        "data": Insignia.carregar_insignia(id)
    }, 200
     
@app.route("/educando/conquista", methods=["POST"])
def post_conquista_insignia():
    if not request.is_json:
        return {"Erro, conteudo deve ser um content-type/json"}, 415

    data = request.get_json()
    educando = Educando.carregar_educando(data["educando_id"])
    insignia = Insignia.carregar_insignia(data["insignia_id"])

    return {
        "data": {
            "status": "success",
            "educando_id": data["educando_id"],
            "educando_nome": educando.nome,
            "insignia_id": data["insignia_id"],
            "insignia_nome": insignia.nome,
            "nivel_insignia": data["nivel_insignia"],
            "data_conquista": data["data_conquista"],
            "data_registro": datetime.now().isoformat()
        }
    }, 201
    
@app.route("/insignias/criar", methods=["POST"])
def post_criar_insiginia():
    # if not request.is_json:
    #     return {"Erro, conteudo deve ser um content-type/json"}, 415
    
    data = request.get_json()
    mensagem = insignia.gravar_insignia()
    if not data.get("nome"):
        return {"error": "O campo 'nome' é obrigatório."}, 400
    if not data.get("trilha"):
        return {"error": "O campo 'trilha' é obrigatório."}, 400
    if not data.get("niveis"):
        return {"error": "O campo 'niveis' é obrigatório."}, 400
    
    insignia = Insignia(data.get("id"),data.get("nome"),data.get("trilha"),data.get("niveis"))
    return {
        "status": "success",
        "message": mensagem
        #"data": data 
    }, 201

@app.route("/educando/criar", methods=['POST'])
def post_criar_educando():
    data = request.get_json()
    educando = Educando(data.get("id"), data.get("nome"),data.get("trilha"), data.get("unidade"), data.get("insignias"))
    mensagem = educando.Gravar_educando()
    return {
        "status": "success",
        "mensagem": mensagem
    }, 201


@app.route("/educando/<int:id>/editar", methods=['PUT'])
def put_atualizar_educando(id):
    data = request.get_json()
    educando = Educando.carregar_educando(id)
    if not educando:
        return ("educando não encontrado"),404
    
    if "nome" in data:
        educando.nome = data["nome"]
    if "trilha" in data:
        educando.trilha = data["trilha"]
    if "unidade" in data:
        educando.unidade = data["unidade"]
    if "insignias" in data:
        educando.insignias = data["insignia"]

    mensagem = educando.atualizar_educando()
    return {
        "status": "success",
        "mensagem" : mensagem
    },201


@app.route("/educando/<int:id>/deletar", methods=['DELETE'])
def delete_deletar_educando(id):
    educando = Educando.carregar_educando(id)
    if not educando:
        return ("educando não encontrado"),404
    if Educando.remover_educando(educando):
        return ("Educando foi deletada com sucesso!"), 200
   

    return {
        "status": "success",
        "educando": educando.to_json(),
    }, 201


@app.route("/insignia/<int:id>/atualizar", methods=['PUT'])
def put_atualizar_insignia(id):
    data = request.get_json()
    insignia = Insignia.carregar_insignia(id)
    if not insignia in data:
        return ("Insignia não encontrada"), 404
    
    if "nome" in data:
        insignia.nome = data["nome"]
    if "trilha" in data:
        insignia.trilha = data["trilha"]
    if "niveis" in data:
        insignia.niveis = data["niveis"]


    mensagem = insignia.atualizada()
    return {
        "status": "success",
        "mensagem": mensagem
    }, 200


@app.route("/insignia/<int:id>/deletar", methods=['DELETE'])
def delete_deletar_insignia(id):
    insignia = Insignia.carregar_insignia(id)
    if not insignia:
        return ("Insígnia não encontrada."), 404
    
    if Insignia.remover_insignia(insignia):
        return ("Insígnia com foi deletada com sucesso!"), 200