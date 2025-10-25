
# Clase abstracta que define una operacion generica

from abc import ABC, abstractclassmethod

class Operacion(ABC):
    @abstractclassmethod
    def ejecutar (self,a,b):
        pass

# Implementacion para suma

class Suma(Operacion):
    def ejecutar(self,a,b):
        return a + b
    

# Implementacion para resta
class Resta(Operacion):
    def ejecutar(self,a,b):
        return a - b
    




# clase calculadora que esta abierta a nuevas operaciones

class Calculadora:
    def __init__(self,operacion:Operacion):
        self.operacion = operacion

    def calcular(self,a,b):
        return self.operacion.ejecutar(a,b)

# USO

op_suma = Suma()
calculadora = Calculadora(op_suma)
print(calculadora.calcular(3,5))


op_resta = Resta()
calculadora_dos = Calculadora(op_resta)
print(calculadora_dos.calcular(3,5))

calculadora_suma = Calculadora(Suma())
print(calculadora_suma.calcular(5,3))