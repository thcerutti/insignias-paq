import abc

class Modelo_base:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def to_json(self):
        pass