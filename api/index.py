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
        "data": [
            Educando(1, "Thiago", "SC401", ["Programação"], ["Python", "Javascript"]).to_json(),
            Educando(2, "Maria Perreira", "Pedra Branca", ["Design"], ["Photoshop", "Illustrator"]).to_json(),
            Educando(3, "João da Silva", "SC401", ["Programação", "Design"], ["Python", "Illustrator"]).to_json()
        ]
    }, 200

@app.route("/insignias", methods=["GET"])
def get_insignias():
    requisitos = {
        "python": [
            Nivel_insignia(1, [
                "Leitura de arquivo CSV (Há vários dados no https://www.kaggle.com/datasets).",
                "Transformar e utilizar do arquivo tipos primitivos: int, string, lista, tuplas e dicionários.",
                "Estruturas condicionais e de repetição (if, else, for, while)",
                "Criar métodos",
                "Escrita de um arquivo CSV"
            ]),
            Nivel_insignia(2, [
                "Conexão e manipulação do banco de dados.",
                "Manipulação de strings.",
                "Instalação de módulos externos com PiP.",
                "Aplicação de paradigma funcional com map, reduce, filter e funções lambda."
            ]),
            Nivel_insignia(3, [
                "Criação de API web com Django e Flask."
            ])
        ]
    }
    print(requisitos)
    return {
        "data": [
            Insignia(1, "Python", "Programação", requisitos["python"]).to_json(),
        ]
    }, 200

@app.route("/educando/<int:id>/insignias", methods=["GET"])
def get_insiginias_educando(id):
    return{
        "data":[
    {
        "Nome": "paulo",
        "trilha": "programação",
        "insignias": [
                {
                    "id":1,
                    "nome": "python",
                    "nivel": 2,
                },
                {
                    "id":2,
                    "nome": "logica de programação",
                    "nivel": 3,

                },
                {
                    "id":3,
                    "nome": "javascript",
                    "nivel": 3,

                }
            ]
        }
    ]
}, 200

@app.route("/insignias/<int:id>/requisitos", methods=["GET"])
def get_requisitos(id):
    return{
        "data":[
            {
                "id-insignia":1,
                "nome":"Python",
                "nivel":1,
                "requisitos":"Manipulação de strings"
            }
        ]
}, 200

@app.route("/educando/conquista", methods=["POST"])
def post_conquista_insignia():
    return{
        "data":{
            "status": "success"
        }
    }
