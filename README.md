# Inventario de videojuegos taller

Este proyecto es una aplicación de consola en Python para llevar el inventario de una tienda de videojuegos. Los datos se guardan en SQLite, así que no se pierden cuando se cierra el programa.

## Archivos

- modelo.py: la clase Producto.
- base_datos.py: hace la conexión y crea la tabla.
- producto_dao.py: tiene las consultas SQL.
- producto_servicio.py: valida los datos y aplica las reglas de venta.
- main.py: muestra el menú y llama al servicio.
- inventario.db: se crea sola la primera vez que se ejecuta.

main.py no tiene SQL, todo pasa por el DAO.

## Opciones del menú

1. Registrar un videojuego.
2. Mostrar el inventario.
3. Buscar por ID.
4. Actualizar nombre, precio y stock.
5. Eliminar por ID.
6. Vender unidades.
7. Salir.

El programa no deja meter nombres vacíos, precios de cero o negativos, cantidades negativas, ventas de cero o más unidades de las que hay, y avisa cuando el ID no existe. Si alguien escribe una letra donde va un número, vuelve a pedir el dato y no se cierra.

## Pruebas

Probé estos casos:

- Registrar Resident Evil 4 con precio 180000 y stock 10.
- Mostrar el inventario.
- Buscar un ID que existe.
- Actualizar un producto y comprobar que el cambio queda guardado.
- Vender 3 unidades y ver que el stock baja de 10 a 7.
- Intentar vender 20 unidades y ver que no deja.
- Buscar un ID que no existe.
- Eliminar un producto y ver que ya no sale en el inventario.

## Evidencias

Registrar, buscar, actualizar y vender:

![Operaciones exitosas](evidencias/evidencia_1_operaciones.png)

Validaciones y operaciones rechazadas. El stock sigue en 7 porque quedó guardado de la ejecución anterior:

![Validaciones](evidencias/evidencia_2_validaciones.png)

Eliminar el videojuego con ID 2, que es el Zelda que se registró en la prueba anterior, y mostrar el inventario después. Los IDs los pone SQLite solo, no se escriben al registrar.

![Eliminar producto](evidencias/evidencia_3_eliminar.png)
