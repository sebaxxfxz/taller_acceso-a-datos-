class Producto:
    def __init__(self, nombre, precio, cantidad, id_producto=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return "ID: {} | Nombre: {} | Precio: {} | Stock: {}".format(
            self.id_producto, self.nombre, self.precio, self.cantidad
        )
