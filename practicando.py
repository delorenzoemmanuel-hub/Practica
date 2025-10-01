class Persona():                                   #RELACION DE HERENCIA , CLASE ABSTRACTA
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):                            #METODO ABSTRACTO
        pass

class Padre(Persona):
    pass

    def hablar(self):
        return "padre del pequeño que se presento arriba"   
    
class Hijo(Persona):
    pass

    def hablar(self):
        return "mi papa se llama "
emmanuel = Padre("emmanuel", 36)
valentino = Hijo("valentino", 3)



class Madre(Persona):     
    pass

    def hablar(self):
        return "madre de " + valentino.nombre                           

natalia = Madre("natalia",36)


class Jardin():
    def __init__(self,nombre,salita):
        self.nombre = nombre
        self.salita = salita    
        self.alumno = valentino
        
    def asiste(self):
        pass

    

colegio = Jardin("jardin", "fuxia")
print(f" hola soy, {valentino.nombre},tengo {valentino.edad} años de edad,{valentino.hablar()} {emmanuel.nombre} y tiene {emmanuel.edad}, mi mama es , {natalia.nombre} y tiene {natalia.edad} años de edad")    


    

