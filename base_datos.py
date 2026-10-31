import sqlite3

NOMBRE_BASE = "inventario.db"


def conectar():
    return sqlite3.connect(NOMBRE_BASE)


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videojuegos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()
