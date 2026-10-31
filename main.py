from base_datos import crear_tabla
from producto_servicio import ProductoServicio


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes escribir un numero entero.")


def pedir_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debes escribir un numero valido.")


def mostrar_menu():
    print("\nINVENTARIO DE VIDEOJUEGOS")
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")


def main():
    crear_tabla()
    servicio = ProductoServicio()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre del videojuego: ")
            precio = pedir_decimal("Precio: ")
            cantidad = pedir_entero("Cantidad disponible: ")
            try:
                servicio.registrar_producto(nombre, precio, cantidad)
                print("Producto guardado correctamente.")
            except ValueError as error:
                print("Error:", error)

        elif opcion == "2":
            productos = servicio.listar_productos()
            if len(productos) == 0:
                print("El inventario esta vacio.")
            else:
                print("\nVIDEOJUEGOS REGISTRADOS")
                for producto in productos:
                    print(producto)

        elif opcion == "3":
            id_producto = pedir_entero("ID del videojuego: ")
            try:
                producto = servicio.buscar_producto(id_producto)
                print(producto)
            except ValueError as error:
                print("Error:", error)

        elif opcion == "4":
            id_producto = pedir_entero("ID del videojuego a actualizar: ")
            try:
                servicio.buscar_producto(id_producto)
                nombre = input("Nuevo nombre: ")
                precio = pedir_decimal("Nuevo precio: ")
                cantidad = pedir_entero("Nueva cantidad disponible: ")
                servicio.actualizar_producto(id_producto, nombre, precio, cantidad)
                print("Producto actualizado correctamente.")
            except ValueError as error:
                print("Error:", error)

        elif opcion == "5":
            productos = servicio.listar_productos()
            if len(productos) == 0:
                print("No hay videojuegos para eliminar.")
            else:
                print("\nVIDEOJUEGOS REGISTRADOS")
                for producto in productos:
                    print(producto)
                id_producto = pedir_entero("ID del videojuego a eliminar: ")
                try:
                    servicio.eliminar_producto(id_producto)
                    print("Producto eliminado correctamente.")
                except ValueError as error:
                    print("Error:", error)

        elif opcion == "6":
            id_producto = pedir_entero("ID del videojuego: ")
            cantidad = pedir_entero("Cantidad a vender: ")
            try:
                nuevo_stock = servicio.vender_producto(id_producto, cantidad)
                print("Venta realizada correctamente, Nuevo stock:", nuevo_stock)
            except ValueError as error:
                print("Error:", error)

        elif opcion == "7":
            print("Saliendo del programa")
            break

        else:
            print("Opcion no valida, intentalo de nuevo.")


if __name__ == "__main__":
    main()
