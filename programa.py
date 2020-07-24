import sqlite3
from datetime import datetime   #importe esto para que se actualice el año automaticamente
fecha_y_hora= datetime.now()
from clasePerros import *

conexion = sqlite3.connect("baseDeDatos1.db")
cursor = conexion.cursor()

print("Te damos la bienvenida al refugio canino 'Anfiloquio'\n")

inicio=input("Quieres agregar un nuevo perro al refugio?")

while inicio.lower()=="si":

    print("ok")

    nombreDelPerro = input("nombre del perro-->")
    edadDelPerro = input("edad del perro-->")
    pesoDelPerro = input("peso del perro-->")
    razaDelPerro = input("raza del perro-->")
    anoDeLaUltimaVacuna = int(input("año de la ultima vacuna \n(si lo desconoce digite cero)-->"))

    datosDelPerro= [nombreDelPerro, edadDelPerro, pesoDelPerro,razaDelPerro, anoDeLaUltimaVacuna]

    cursor.execute("INSERT INTO perros VALUES(?,?,?,?,?)", datosDelPerro)


    print("'has ingresado a  "+nombreDelPerro.upper()+ "  con exito")

    resultado = fecha_y_hora.year - anoDeLaUltimaVacuna

    if (0<=resultado<=2):

        print(nombreDelPerro.upper(), "'esta al dia con sus vacunas'\n")

    else:
        print("'se deben actualizar las vacunas de' ",nombreDelPerro.upper(),"\n")

    inicio2=input("quiere ingresar otro perro en el refugio?")

    if (inicio2.lower()=="no"):

        inicio=inicio2

else:
    buscar1= input("quiere revisar los datos de un perro ingresado en nuestro refugio?")

    if (buscar1.lower()=="si"):

       nombreDelPerro = input("ingrese el nombre del perro a consultar-->")
       perros=cursor.execute("SELECT * FROM perros WHERE nombre=?", (nombreDelPerro,))
       query = "SELECT * FROM perros where nombre = ?"
       for perro in perros:
        print("nombre-->",perro[0])
        print("edad-->", perro[1])
        print("peso-->", perro[2])
        print("raza-->", perro[3])
        print("fecha de la ultima vacuna-->", perro[4])

    print("---------    gracias por su visita    ----------")

conexion.commit()
conexion.close()