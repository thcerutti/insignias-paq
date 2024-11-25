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
    return [
      Insignia(1, "Python", "Programação", [
        Nivel_insignia(1, [
            "Leitura de arquivo CSV (Há vários dados no https://www.kaggle.com/datasets).",
            "Transformar e utilizar do arquivo tipos primitivos: int, string, lista, tuplas e dicionários.",
            "Estruturas condicionais e de repetição (if, else, for, while)",
            "Criar métodos",
            "Escrita de um arquivo CSV"
        ]),
        Nivel_insignia(2, [
            "Conexão e manipulação do banco de dados.",
            "Manipulação de strings.",
            "Instalação de módulos externos com PiP.",
            "Aplicação de paradigma funcional com map, reduce, filter e funções lambda."
        ]),
        Nivel_insignia(3, [
            "Criação de API web com Django e Flask."
        ])
      ])
    ]
    
  def gravar_insignia(self):
    return (
     "A insignia" + self.nome + "foi salva com sucesso"
    )
  
  def insignia_atualizada(self):
        return (
            "A insígnia " + self.nome + " foi atualizada com sucesso."
        )
  
  def remover_insignia(insignia):
    lista_insignia = Insignia.listar_insignias()
    if insignia in lista_insignia:
      lista_insignia.remove(insignia)


  def to_json(self):
    return {
      "id": self.id,
      "nome": self.nome,
      "trilha": self.trilha,
      "niveis": [nivel.to_json() for nivel in self.niveis]
    }
  
  
