from models.modelo_base import Modelo_base
import json

class Educando(Modelo_base):
    def __init__ (self, id, nome, trilha, unidade, insignias):
        self.id = id
        self.nome = nome
        self.trilha = trilha
        self.unidade = unidade
        self.insignias = insignias

    @staticmethod
    def listar_insignias(educando_id):
        return [educando for educando in Educando.Listar_educandos() if educando.id == educando_id]

    @staticmethod
    def carregar_educando(id):
        educandos = [educando for educando in Educando.Listar_educandos() if educando.id == id]
        return educandos[0] if educandos else None

    @staticmethod
    def Listar_educandos():
        listaDeEducandos = []
        with open('data/educandos.json', 'r') as file:
            educandos = json.load(file)
            for educando in educandos:
                listaDeEducandos.append(Educando(educando["id"], educando["nome_completo"], educando["trilha"], educando["unidade"], educando["insignias"]))

        return listaDeEducandos

    def to_json (self):
        return {
        "id": self.id,
        "nome_completo": self.nome,
        "unidade": self.unidade,
        "trilha": self.trilha,
        "insignias": self.insignias
    }
