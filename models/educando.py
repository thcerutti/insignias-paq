class Educando:
  def __init__(self, id, nome_completo, unidade, trilhas, insignias):
    self.id = id
    self.nome_completo = nome_completo
    self.unidade = unidade
    self.trilhas = trilhas
    self.insignias = insignias

  def registrar_conquista_de_insignia(self, insignia):
    self.insignias.append(insignia)

  def to_json(self):
    return {
      "id": self.id,
      "nome_completo": self.nome_completo,
      "unidade": self.unidade,
      "trilhas": self.trilhas,
      "insignias": self.insignias
    }
