# PATRON CREADOR: Asigna la responsabilidad de crear una instancia de una clase B a una clase A si A contiene, usa o tiene una relación cercana con B.“Es decir, si un objeto
#necesita otro para funcionar o tiene una fuerte relación con él, entonces debe ser responsable de crearlo.


class Itempedido:  # CLASE QUE REPRESENTA UN ITEM DENTRO DE PEDIDO
    def __init__(self, nombre_producto,cantidad):
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad

class Pedido: #CLASE QUE REPRESENTA UN PEDIDO Y EJECUTA EL PATRON CREADOR
    def __init__(self):
        self.item = []

    def agregar_item(self,nombre_producto,cantidad):  #METODO QUE APLICA GRASP : CREADOR
        item = Itempedido(nombre_producto,cantidad)
        self.item.append(item)


    def mostrar_pedido(self):
        print("Pedido:")
        for item in self.item:
            print(f"{item.nombre_producto}:{item.cantidad}")
        
pedido = Pedido()
pedido.agregar_item("salsa de tomate", 5)
pedido.agregar_item("arroz", 5)
pedido.mostrar_pedido()



productos = Pedido()
productos.agregar_item("salsa de tomate", 5)
productos.mostrar_pedido