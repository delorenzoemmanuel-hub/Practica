from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    @abstractmethod
    def delivery(self):
        pass

class Auto(Vehiculo):
    def delivery(self):
        return super().delivery()