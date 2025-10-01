import random
import time

class Caballo(object):
    def __init__(self, name):
        self.name = name
        self.posicion = 0
    
    def corre(self):
        p = random.randint(1,5)
        self.posicion = self.posicion + p

    def dibuja(self):
        x = (" " * self.posicion) + f"[{self.name}]"
        print(x)

c = Caballo("yatasto")
i = 0
while i < 5 :
    c.corre()
    c.dibuja()
    i = i + 1
    time.sleep(1)
    