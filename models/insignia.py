from models.modelo_base import Modelo_base

class Insignia(Modelo_base):

  def __init__(self, id, nome, trilha, niveis):
    self.id = id
    self.nome = nome
    self.trilha = trilha
    self.niveis = niveis

  def to_json(self):
    return {
      "id": self.id,
      "nome": self.nome,
      "trilha": self.trilha,
      "niveis": [nivel.to_json() for nivel in self.niveis]
    }
