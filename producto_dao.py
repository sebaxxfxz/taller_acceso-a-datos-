from base_datos import conectar
from modelo import Producto


class ProductoDao:

    def registrar(self, producto):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO videojuegos (nombre, precio, cantidad) VALUES (?, ?, ?)",
            (producto.nombre, producto.precio, producto.cantidad)
        )
        conexion.commit()
        conexion.close()

    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, cantidad FROM videojuegos")
        filas = cursor.fetchall()
        conexion.close()

        productos = []
        for fila in filas:
            producto = Producto(fila[1], fila[2], fila[3], fila[0])
            productos.append(producto)
        return productos

    def buscar(self, id_producto):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, precio, cantidad FROM videojuegos WHERE id = ?",
            (id_producto,)
        )
        fila = cursor.fetchone()
        conexion.close()

        if fila is None:
            return None
        return Producto(fila[1], fila[2], fila[3], fila[0])

    def actualizar(self, producto):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE videojuegos SET nombre = ?, precio = ?, cantidad = ? WHERE id = ?",
            (producto.nombre, producto.precio, producto.cantidad, producto.id_producto)
        )
        conexion.commit()
        cambiadas = cursor.rowcount
        conexion.close()
        return cambiadas > 0

    def eliminar(self, id_producto):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM videojuegos WHERE id = ?", (id_producto,))
        conexion.commit()
        eliminadas = cursor.rowcount
        conexion.close()
        return eliminadas > 0

    def actualizar_cantidad(self, id_producto, cantidad):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE videojuegos SET cantidad = ? WHERE id = ?",
            (cantidad, id_producto)
        )
        conexion.commit()
        conexion.close()
