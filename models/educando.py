from models.modelo_base import Modelo_base
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client["meuBanco"]
educandos_collection = db["educandosCollection"]

class Educando(Modelo_base):
    def __init__(self, id, nome, trilha, unidade, insignias):
        self.id = id
        self.nome = nome
        self.trilha = trilha
        self.unidade = unidade
        self.insignias = insignias or []

    @staticmethod
    def listar_educandos_com_insignia_conquistada(insignia_id):
        educandos = []
        for educando in Educando.listar_educandos():
            for insignia in educando.insignias:
                if insignia["id"] == insignia_id:
                    educandos.append(educando)
        return educandos

    @staticmethod
    def listar_insignias(educando_id):
        educando = Educando.carregar_educando(educando_id)
        return educando.insignias if educando else []

    @staticmethod
    def carregar_educando(educando_id):
        document = educandos_collection.find_one({"_id": ObjectId(educando_id)})
        if not document:
            return None
        return Educando.from_dict(document)

    @staticmethod
    def listar_educandos():
        documents = educandos_collection.find()
        return [Educando.from_dict(doc) for doc in documents]

    def gravar_educando(self):
        data = self.to_dict()

        if self.id:
            educandos_collection.update_one({"_id": ObjectId(self.id)}, {"$set": data})
            return f"Educando {self.nome} atualizado com sucesso!"

        else:
            result = educandos_collection.insert_one(data)
            self.id = str(result.inserted_id)
            return f"Educando {self.nome} salvo com sucesso!"

    def atualizar_educando(self):
        return (
             "O educando(a)" + self.nome +  "foi atualizado com sucesso"
        )

    def remover_educando(educando):
        lista_educando = Educando.Listar_educandos()
        if educando in lista_educando:
            lista_educando.remove(educando)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "trilha": self.trilha,
            "unidade": self.unidade,
            "insignias": [{
                "id": insignia["id"],
                "nome": insignia["nome"],
                "nivel": insignia["nivel"],
                "data": insignia["data"]
            } for insignia in self.insignias]
        }

    @staticmethod
    def from_dict(data):
        return Educando(
            id=str(data["_id"]),
            nome=data["nome"],
            trilha=data["trilha"],
            unidade=data["unidade"],
            insignias=data["insignias"]
        )

