#BAJO ACOPLAMIENTO: MIDE LA DEPENDENCIA ENTRE CLASES, CUANTO MENOS DEPENDAN UNA DE OTRA, MEJOR.

# EJEMPLO DE UN "ALTO" ACOPLAMIENTO

class Motor:
    def encender(self):
        print("el motor esta encendido")


class Coche:
    def __init__(self):
        self.motor = Motor()  # coche fuertemente acoplado a motor

    def conducir(self):
        self.motor.encender()  
        print("el coche esta en movimiento")

coche = Coche()
coche.conducir()


# EJEMPLO DE UN "ALTO" ACOPLAMIENTO

class Motor:
    def encender(self):
        print("el motor esta encendido")

class motor_electrico:
    def encender(self):
        print("el motor electrico esta encendido")

class Coche:
    def __init__(self,motor):
        self.motor = motor

    def conducir(self):
        self.motor.encender()
        print("el coche esta en movimiento")

motor_gasolina = Motor()
coche_gasolina = Coche(motor_gasolina)
coche_gasolina.conducir