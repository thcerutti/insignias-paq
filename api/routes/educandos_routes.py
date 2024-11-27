from flask import Blueprint, request
from datetime import datetime
from models.educando import Educando
from models.insignia import Insignia

educandos_bp = Blueprint("educandos", __name__)

@educandos_bp.route("/educandos", methods=["GET"])
def get_educandos():
    try:
        return [educando.to_dict() for educando in Educando.listar_educandos()], 200
    except Exception as e:
        return {"error": str(e)}, 500

@educandos_bp.route("/educando/<id>/insignias", methods=["GET"])
def get_insignias_educando(id):
    educando = Educando.carregar_educando(id)
    if not educando:
        return {"error": "Educando não encontrado"}, 404

    return {
        "data": {
            "educando_id": id,
            "educando_nome": educando.nome,
            "insignias": educando.insignias
        }
    }, 200

@educandos_bp.route("/educando/conquista", methods=["POST"])
def post_conquista_insignia():
    if not request.is_json:
        return {"error": "Conteúdo deve ser JSON"}, 415

    data = request.get_json()

    educando = Educando.carregar_educando(data.get("educando_id"))
    insignia = Insignia.carregar_insignia(data.get("insignia_id"))

    if not educando or not insignia:
        return {"error": "Educando ou Insignia não encontrado"}, 404

    return {
        "data": {
            "status": "success",
            "educando": {
                "id": data["educando_id"],
                "nome": educando.nome,
            },
            "insignia": {
                "id": data["insignia_id"],
                "nome": insignia.nome,
                "nivel": data.get("nivel_insignia"),
            },
            "data_conquista": data.get("data_conquista"),
            "data_registro": datetime.now().isoformat()
        }
    }, 201

@educandos_bp.route("/educando/criar", methods=["POST"])
def post_criar_educando():
    if not request.is_json:
        return {"error": "Conteúdo deve ser JSON"}, 415

    data = request.get_json()
    educando = Educando(
        nome=data.get("nome"),
        trilha=data.get("trilha"),
        unidade=data.get("unidade"),
        insignias=data.get("insignias", [])
    )

    mensagem = educando.gravar_educando()

    return {
        "status": "success",
        "mensagem": mensagem,
        "data": educando.to_dict()
    }, 201

@educandos_bp.route("/educando/<id>/editar", methods=['PUT'])
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

@educandos_bp.route("/educando/<id>/deletar", methods=['DELETE'])
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
