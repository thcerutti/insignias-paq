from models.modelo_base import Modelo_base

class Nivel_insignia(Modelo_base):
  def __init__(self, id, requisitos):
    self.id = id
    self.requisitos = requisitos

  def to_json(self):
    return {
      "id": self.id,
      "requisitos": self.requisitos
    }
