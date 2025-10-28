class singleton:
    _instance = None

    def __new__(cls,nombre,edad):
        if not cls._instance:
            cls._instance = super(singleton, cls).__new__(cls)
            cls._instance.nombre = nombre
            cls._instance.edad = edad
        return cls._instance
    
singleton1 = singleton("emmanue",36)
singleton2 = singleton("marcelo",38)

print(singleton1 is singleton2)

print(singleton1.nombre,singleton1.edad)
print(singleton2.nombre, singleton2.edad)