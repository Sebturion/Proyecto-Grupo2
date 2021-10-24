from sqlite3.dbapi2 import Error

from werkzeug.security import check_password_hash, generate_password_hash

import db


class Usuario():

    def __init__(self, NOMBRE, CONTACTO, EMAIL, CONTRASENA):
        self.nombre = NOMBRE
        self.contacto = CONTACTO
        self.email = EMAIL
        self.contrasena = CONTRASENA

    #registro de usuario
    def insert(self):
        try:
            hashedContrasena = generate_password_hash(self.contrasena, method="pbkdf2:sha256", salt_length=32)
            sql = "INSERT INTO usuario (nombre_apellido, num_contacto, email, contrasena, rol_usuario) VALUES (?,?,?,?,?);"
            objeto = db.ejecutarCUD(sql, [self.nombre, self.contacto, self.email, hashedContrasena, 'usuario'])
            return (objeto > 0)
        except:
            print("Error en el registro de usuario" + str(Error))


    def autenticacionUsuario(self):
        try:
            sql = "SELECT * FROM usuario WHERE email = ?"
            objeto = db.ejecutarRead(sql, [self.email])

            if objeto:
                if check_password_hash(objeto[0]['contrasena'], self.contrasena):
                    return True
                
            return False
        except:
            print("Error en la autenticacion de usuario" + str(Error))



class Vuelos:
    @staticmethod
    def mostarVuelos(LUGAR):
        try:
            if LUGAR:
                sql = "SELECT * FROM vuelo WHERE origen_vuelo = ? OR destino_vuelo = ?"
                return db.ejecutarRead(sql, [LUGAR, LUGAR])
            else:
                sql = "SELECT * FROM vuelo"
                return db.ejecutarRead(sql, None)
        except:
            print("Error al ejecutar select. " + str(Error))



    