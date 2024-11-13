from models.modelo_base import Modelo_base

class Requisito_insignia(Modelo_base):
  def __init__(self, id, descricao):
    self.id = id
    self.descricao = descricao

  def to_json(self):
    return {
      "id": self.id,
      "descricao": self.descricao
    }
