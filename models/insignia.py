from models.modelo_base import Modelo_base
from models.nivel_insignia import Nivel_insignia
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client["meuBanco"]
insignias_collection = db["insigniasCollection"]

class Insignia(Modelo_base):
    def __init__(self, id, nome, trilha, niveis):
        self.id = id
        self.nome = nome
        self.trilha = trilha
        self.niveis = [Nivel_insignia(**nivel) if isinstance(nivel, dict) else nivel for nivel in (niveis or [])]

    @staticmethod
    def carregar_insignia(insignia_id):
        if not ObjectId.is_valid(insignia_id):
            raise ValueError(f"ID inválido: {insignia_id}")

        document = insignias_collection.find_one(filter={"_id": ObjectId(insignia_id)})
        print(document["nome"] + " - " + insignia_id)
        if not document:
            return None
        return Insignia.from_dict(document)

    @staticmethod
    def listar_insignias():
        documents = insignias_collection.find()
        return [Insignia.from_dict(doc) for doc in documents]

    def gravar_insignia(self):
      data = self.to_dict()
      if self.id:
          insignias_collection.update_one({"_id": ObjectId(self.id)}, {"$set": data})
          return f"Insígnia {self.nome} atualizada com sucesso!"
      else:
          result = insignias_collection.insert_one(data)
          self.id = str(result.inserted_id)
          return f"Insígnia {self.nome} salva com sucesso!"

    def insignia_atualizada(self):
          return (
              "A insígnia " + self.nome + " foi atualizada com sucesso."
          )

    def remover_insignia(insignia):
      lista_insignia = Insignia.listar_insignias()
      if insignia in lista_insignia:
        lista_insignia.remove(insignia)

    def to_dict(self):
            data = {
                "nome": self.nome,
                "trilha": self.trilha,
                "niveis": [
                   nivel.to_dict() if isinstance(nivel, Nivel_insignia) else nivel
                   for nivel in self.niveis
                ],
            }
            if self.id:
                data["_id"] = self.id
            return data

    @staticmethod
    def from_dict(data):
        return Insignia(
            id=str(data["_id"]),
            nome=data["nome"],
            trilha=data["trilha"],
            niveis=[Nivel_insignia.from_dict(nivel) for nivel in data.get("niveis", [])]

        )

