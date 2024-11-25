from models.modelo_base import Modelo_base
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://pedrorochaneni:<senha>@paq-insignias.qmjh0.mongodb.net/")  
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

    def to_dict(self):
        return {
            "nome": self.nome,
            "trilha": self.trilha,
            "unidade": self.unidade,
            "insignias": self.insignias
        }

    @staticmethod
    def from_dict(data):
        return Educando(
            id=str(data["_id"]),
            nome=data["nome"],
            trilha=data["trilha"],
            unidade=data["unidade"],
            insignias=data.get("insignias", [])
        )

