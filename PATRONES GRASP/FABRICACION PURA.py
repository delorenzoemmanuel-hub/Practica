# FABRICACION PURA PROPONE CREAR UNA CLASE ARTIFICIAL QUE SE OCUPE DE METODOS SECUNDARIOS 
# Y DEJARLE LA RESPONSABILIDAD PRIMARIA PURA Y EXCLUSIVAMENTE A LA CLASE PRINCIPAL

class Pedido: 
    def __init__(self, id_pedido, descripcion):
        self.id_pedido = id_pedido
        self.descripcion = descripcion

class RepositorioPedidos:  #se crea la clase RepositorioPedido para que guarde los pedidos y sacarle esa responsabilidad a la clase pedidos
    def guardar(self, pedido):
        print( f"Guardando el pedido {pedido.id_pedido}: {pedido.descripcion}")

        
