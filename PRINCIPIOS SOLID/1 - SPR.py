
#PRINCIPIO SOLID 1 - PRINCIPIO DE RESPONSABILIDAD UNICA (SPR)

#INCORRECTO

class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email

    def enviar_email(self):
        pass

    def guarda_email(self):
        pass

#CORRECTO
class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email

class Sercivio_de_email:
     def Enviar_email (self,email,mensaje):
         pass
    

class Servicio_de_usuario:
    def guardar_email (self,usuario):
        pass 