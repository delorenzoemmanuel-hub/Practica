class Pedido:
    def __init__(self):
        self.item = []
        self.total = 0.0

    def agregar_item(self,nombre,precio,cantidad):
        item = {"nombre":nombre,"precio":precio,"cantidad":cantidad}
        self.item.append(item)
        self.actualizar_total(precio,cantidad)

    def actualizar_total(self,precio,cantidad):
        self.total += precio * cantidad

    def mostrar_pedido(self):
        for item in self.item:
            print(f"Producto:{item['nombre']},cantidad: {item['cantidad']},precio: {item['precio']}")
        print(f"Total a pagar:{self.total}")

pedido = Pedido()
pedido.agregar_item("tomate",3,5)
pedido.agregar_item("choclo",4,7)
pedido.mostrar_pedido()