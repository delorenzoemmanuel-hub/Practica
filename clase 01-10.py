class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad




base_datos = [
    "Nombre,Apellido,Edad",
    "Emmiliano,Billi,43"
    "Emmanuel,Delorenzo,34",
    "cesar,Billi,11"]

s = "cesar,Billi,11"
valores = s.split(",")
print(valores)