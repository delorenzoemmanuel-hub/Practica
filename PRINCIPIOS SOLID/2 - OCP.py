#PRINCIPIO SOLID 2 - PRINCIPIO ABIERTO CERRADO (OCP)

#INCORRECTO  poder agregar solo editando el codigo ya existente

class Forma:  
    def dibujar_cuadrado(self):
        print("Dibujar un cuadrado")

    def  dibujar_circulo(self):
        print("Dibujar un circulo")

form = Forma()
#form.dibujar_circulo()


#CORRECTO   poder agregar sin modificar el codigo existente

class Forma:
    def dibujar(self):
        pass

class Cuadrado(Forma):
    def dibujar(self):
        print("Dibujar un cuadrado")

class Circulo(Forma):
    def dibujar(self):
        return "Dibujar un circulo"


form = Circulo()
print(form.dibujar())
####################################


