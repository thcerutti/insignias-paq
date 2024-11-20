import json
from models.modelo_base import Modelo_base
from models.nivel_insignia import Nivel_insignia

class Insignia(Modelo_base):

  def __init__(self, id, nome, trilha, niveis):
    self.id = id
    self.nome = nome
    self.trilha = trilha
    self.niveis = niveis

  @staticmethod
  def carregar_insignia(id):
    insignia = [insignia.to_json() for insignia in Insignia.listar_insignias() if insignia.id == id]
    return insignia[0] if insignia else None

  @staticmethod
  def listar_insignias():
    listaDeInsignias = []
    with open('data/insignias.json', 'r') as file:
        insignias = json.load(file)
        for insignia in insignias:
            niveisDaInsignia = []
            for nivel in insignia["niveis"]:
                niveisDaInsignia.append(Nivel_insignia(nivel["id"], nivel["requisitos"]))
            listaDeInsignias.append(Insignia(insignia["id"], insignia["nome"], insignia["trilha"], niveisDaInsignia))
    return listaDeInsignias

  def gravar_insignia(self):
    return (
      self.nome + "foi salva com sucesso"
    )

  def to_json(self):
    return {
      "id": self.id,
      "nome": self.nome,
      "trilha": self.trilha,
      "niveis": [nivel.to_json() for nivel in self.niveis]
    }
