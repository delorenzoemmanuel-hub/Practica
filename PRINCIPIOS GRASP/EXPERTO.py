class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_impuesto(self,tasa_impuesto):
        return self.salario * tasa_impuesto
    

empleado = Empleado("Emmanuel", 1000000)
tasa_impuesto = 0.2
impuesto = empleado.calcular_impuesto( tasa_impuesto)
print(impuesto)