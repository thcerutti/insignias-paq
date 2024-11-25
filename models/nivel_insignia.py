from models.modelo_base import Modelo_base

class Nivel_insignia:
    def __init__(self, id=None, requisitos=None):
        self.id = id
        self.requisitos = requisitos or []

    def to_dict(self):
        return {
            "id": self.id,
            "requisitos": self.requisitos,
        }
    @staticmethod
    def from_dict(data):
        return Nivel_insignia(
            id=data["id"],
            requisitos=data["requisitos"]
        )