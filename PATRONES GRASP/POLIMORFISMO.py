class Animal:
    def __init__(self):
        self.patas = 4
        self.cabeza = 1
        self.cola = 1

    def genera_sonido(self):
        pass

class Perro (Animal):

    def genera_sonido(self):
        print("GUAU, GUAU")


class Gato(Animal):

    def genera_sonido(self):
        print("MIAU, MIAU")


perro = Perro()
perro.genera_sonido()
gato = Gato()
gato.genera_sonido()