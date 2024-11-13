
from models.modelo_base import Modelo_base

class Educando(Modelo_base):
  def __init__(self, id, nome_completo, unidade, trilhas, insignias):
    self.id = id
    self.nome_completo = nome_completo
    self.unidade = unidade
    self.trilhas = trilhas
    self.insignias = insignias

  def registrar_conquista_de_insignia(self, insignia):
    self.insignias.append(insignia)

  @staticmethod
  def listar_insignias(educando_id):
    return [educando for educando in Educando.listar_educandos() if educando.id == educando_id]


  @staticmethod
  def listar_educandos():
    return [
      Educando(1, "Matheus Pires", "SC401", ["Programação"], ["Python", "Javascript"]),
      Educando(2, "Maria Perreira", "Pedra Branca", ["Design"], ["Photoshop", "Illustrator"]),
      Educando(3, "João da Silva", "SC401", ["Programação", "Design"], ["Python", "Illustrator"])
    ]

  def to_json(self):
    return {
      "id": self.id,
      "nome_completo": self.nome_completo,
      "unidade": self.unidade,
      "trilhas": self.trilhas,
      "insignias": self.insignias
    }
