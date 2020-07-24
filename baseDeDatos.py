import sqlite3

conexion= sqlite3.connect("baseDeDatos1.db")

conexion.commit()
conexion.close()