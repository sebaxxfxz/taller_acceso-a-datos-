from modelo import Producto
from producto_dao import ProductoDao


class ProductoServicio:

    def __init__(self):
        self.dao = ProductoDao()

    def validar_datos(self, nombre, precio, cantidad):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

    def registrar_producto(self, nombre, precio, cantidad):
        self.validar_datos(nombre, precio, cantidad)
        producto = Producto(nombre.strip(), precio, cantidad)
        self.dao.registrar(producto)

    def listar_productos(self):
        return self.dao.listar()

    def buscar_producto(self, id_producto):
        producto = self.dao.buscar(id_producto)
        if producto is None:
            raise ValueError("No existe un videojuego con el ID {}.".format(id_producto))
        return producto

    def actualizar_producto(self, id_producto, nombre, precio, cantidad):
        self.validar_datos(nombre, precio, cantidad)
        producto = self.buscar_producto(id_producto)
        producto.nombre = nombre.strip()
        producto.precio = precio
        producto.cantidad = cantidad
        self.dao.actualizar(producto)

    def eliminar_producto(self, id_producto):
        self.buscar_producto(id_producto)
        self.dao.eliminar(id_producto)

    def vender_producto(self, id_producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")

        producto = self.buscar_producto(id_producto)

        if cantidad > producto.cantidad:
            raise ValueError(
                "No hay suficientes unidades. Solo quedan {}.".format(producto.cantidad)
            )

        nuevo_stock = producto.cantidad - cantidad
        self.dao.actualizar_cantidad(id_producto, nuevo_stock)
        return nuevo_stock
