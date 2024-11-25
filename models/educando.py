from models.modelo_base import Modelo_base

class Educando(Modelo_base):
    def __init__ (self, id, nome, trilha, unidade, insignias):
        self.id = id
        self.nome = nome
        self.trilha = trilha
        self.unidade = unidade
        self.insignias = insignias
        
    @staticmethod
    def listar_insignias(educando_id):
        return [educando for educando in Educando.Listar_educandos() if educando.id == educando_id]
     
    @staticmethod
    def carregar_educando(id):
        educandos = [educando for educando in Educando.Listar_educandos() if educando.id == id]
        return educandos[0] if educandos else None
    
    @staticmethod   
    def Listar_educandos():
        return[
            Educando(1, "Nilberto", "PEDRA BRANCA", ["Programação"],  ["JAVA", "PYTHON"]),
            Educando(2, "Joilson", "SC401", ["Programação"], ["Cookie", "Academia"]),
        ]
    
    def Gravar_educando(self):
        return (
         "O educando(a)" + self.nome +  "foi salvo com sucesso" 
        )


    def atualizar_educando(self):
        return (
             "O educando(a)" + self.nome +  "foi atualizado com sucesso" 
        )
    
    def remover_educando(educando):
        lista_educando = Educando.Listar_educandos()
        if educando in lista_educando:
            lista_educando.remove(educando)


    def to_json (self):
        return { 
        "id": self.id,
        "nome_completo": self.nome,
        "unidade": self.unidade,
        "trilha": self.trilha,
        "insignias": self.insignias
        
    }

