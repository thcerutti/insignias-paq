from flask import Flask
from flask_cors import CORS

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
        {
            "id": 1,
            "nome_completo": "Maria da Silva",
            "trilha": "Programação",
            "unidade": "SC401"
        },
        {
            "id": 2,
            "nome_completo": "João da Silva",
            "trilha": "Design",
            "unidade": "Pedra Branca"
        },
    ]
}, 200