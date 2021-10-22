import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect("db/aeropuerto.db")
        return conexion
    except Error as error:
        print("No se pudo conectar a la base de datos. Error: " + error)
        return None

#Create - Update - Delete
def ejecutarCUD(_sql, valores):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            filas = cursor.execute(_sql, valores).rowcount

            cursor.close()
            conexion.commit()
            conexion.close()

            return filas
        else:
            print("No se pudo conectar a la base de datos")
            return -1
    except Error as error:
        print("No se pudo ejecutar la sentencia SQL: " + str(error))
        return -1


def ejecutarRead(_sql, valores):
    try:
        conexion = conectar()
        if conexion:
            conexion.row_factory = convertir_diccionarios
            cursor = conexion.cursor()

            if valores:
                cursor.execute(_sql, valores)
            else:
                cursor.execute(_sql, None)

            filas = cursor.fetchall()
            cursor.close()
            conexion.close()

            return filas
        else:
            print("No se pudo conectar a la base de datos")
            return None
    except Error as error:
        print("No se pudo ejecutar la sentencia SQL: " + str(error))
        return None


def convertir_diccionarios(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    
    return d