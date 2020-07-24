#Todo Perro deberá tener los siguientes atributos: id, nombre, edad, peso, raza, fecha de última vacunación
# (se registrará un número entero para el año únicamente)

import sqlite3
conexion= sqlite3.connect("baseDeDatos1.db")

cursor= conexion.cursor()

cursor.execute("CREATE TABLE perros (nombre TEXT, edad INT, peso INT, raza TEXT, tiempoDesdeUltimaVacuna INT)")

conexion.commit()
conexion.close()
