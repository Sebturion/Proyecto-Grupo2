from logging import debug
from flask import Flask, render_template, request, redirect, url_for, jsonify
from forms import buscarVuelos, formularioLogin, formularioRegistro, verificar_comentarios
import os
from models import *



app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/vuelos', methods=['GET', 'POST'])
def vuelos():
    if (request.method == 'GET'):
        objeto = Vuelos.mostarVuelos(None)
        if objeto:
            return render_template('vuelos.html', vuelos = objeto)
        else:
            return render_template('vuelos.html', mensaje = "En este momento no hay ofertas de vuelos.")
    elif (request.method == 'POST'):
        lugar = request.form['txtBuscador_vuelo']
        objeto = Vuelos.mostarVuelos(lugar)
        if objeto:
            return render_template('vuelos.html', vuelos = objeto)
        else:
            if lugar == "":
                return render_template('vuelos.html', mensaje = "En este momento no hay ofertas de vuelos.")
            else:
                return render_template('vuelos.html', mensaje = ("En este momento no hay ofertas de vuelos a " + lugar))



@app.route('/destinos', methods=['GET', 'POST'])
def destinos():
    if (request.method == 'GET'):
        objeto = Destinos.mostrarDestinos(None)
        if objeto:
            return render_template('destinos.html', destinos = objeto)
        else:
            return render_template('destinos.html', mensaje = "En este momento no hay destinos disponibles.")
    elif (request.method == 'POST'):
        destino = request.form['txtBuscador_destinos']
        objeto = Destinos.mostrarDestinos(destino)
        if objeto:
            return render_template('destinos.html', destinos = objeto)
        else:
            if destino == "":
                return render_template('destinos.html', mensaje = ("Porfavor indique el destino que desea buscar"))
            else:
                return render_template('destinos.html', mensaje = ("No se encontró destino para " + destino))



@app.route('/inicio-sesion', methods=['GET', 'POST'])
def login():
    formulario = formularioLogin(request.form)
    if (request.method == 'GET'):
        return render_template('login.html', form = formularioLogin())
    elif (request.method == 'POST'):
        if formulario.validate_on_submit():
            email_recibido = formulario.correo.data
            contrasenia_recibida = formulario.contrasena.data

            email_admin = 'admin@gmail.com'
            contrasenia_admin = '123456'

            email_piloto = 'piloto@gmail.com'
            contrasenia_piloto = '123456'

            email_usuario_final = 'final@gmail.com'
            contrasenia_usuario_final = '123456'

            if (email_recibido == email_usuario_final and contrasenia_recibida == contrasenia_usuario_final):
                return redirect(url_for('reservar_vuelos'))

            if (email_recibido == email_piloto and contrasenia_recibida == contrasenia_piloto):
                return redirect(url_for('vuelos_asignados'))

            if (email_recibido == email_admin and contrasenia_recibida == contrasenia_admin):
                return redirect(url_for('programar_vuelos'))
        
 

@app.route('/registrarse', methods=['GET','POST'])
def registrarse():
    if request.method == 'GET':
        return render_template("registrarse_usuario.html", form = formularioRegistro())
    elif request.method == 'POST':
        formulario = formularioRegistro(request.form)
        
        error = False
        if formulario.confirmar.data != formulario.contrasena.data:
            error = True

        if (formulario.validate_on_submit()) and (not error):
            nuevoUsuario = Usuario(formulario.nombreApellido.data, formulario.numeroContacto.data, formulario.correo.data, formulario.contrasena.data)
            if nuevoUsuario.insert():
                return render_template("registrarse_usuario.html", form = formularioRegistro(), mensaje = "Registro exitoso")
            else:
                return render_template("registrarse_usuario.html", form = formularioRegistro(), mensaje = "Registro fallido. Consulte con soporte tecnico")
        
        return render_template("registrarse_usuario.html", form = formulario, mensaje = "Registro fallido")



@app.route('/pilotos-registrados', methods=['GET'])
def pilotos_registrados():
    return render_template('pilotos_registrados.html')

@app.route('/configuracion_plataforma_usuario', methods=['GET'])
def configuracion_plataforma_usuario():
    return render_template('configuracion_plataforma_usuario.html')

@app.route('/comentarios-admin', methods=['GET'])
def comentarios_admin():
    return render_template('comentarios_admin.html')

@app.route('/usuarios-registrados', methods=['GET'])
def usuarios_registrados():
    return render_template('usuarios_registrados.html')

@app.route('/configuracion-piloto', methods=['GET'])
def configuracion_piloto():
    return render_template('configuracion_piloto.html')

@app.route('/vuelos-asignados', methods=['GET'])
def vuelos_asignados():
    return render_template('vuelos_asignados.html')


@app.route('/verificar-vuelos', methods = ['GET','POST'])
def verificar_vuelos():
    if request.method == 'GET':
        return render_template('plataforma_usuario_verificar.html', form = verificar_comentarios())
    elif request.method == 'POST':
        formulario = verificar_comentarios(request.form)
        objeto = Vuelos.vueloCodigo(str(formulario.codigo.data))
        if objeto:
            return render_template('plataforma_usuario_verificar.html', form = verificar_comentarios(), vuelo = objeto)
        else:
            print("no existe")




@app.route('/programar-vuelos', methods=["GET", "POST"])
def programar_vuelos():
    listaDestinos = Destinos.listaDestinos()
    if request.method == 'GET':
        formulario = buscarVuelos(request.form)
        return render_template('programar_vuelos_admin.html', form = buscarVuelos(), destinos = listaDestinos)
    elif request.method == 'POST':
        formulario = buscarVuelos(request.form)
        origen = request.form['origen']
        destino = request.form['destino']

        if (origen != '') and (destino != '') and (formulario.fecha.data != None) and (formulario.hora.data != None) and (formulario.minimo.data != None) and (formulario.maximo.data != None):
            objeto = Vuelos.buscarVuelos(origen, destino, str(formulario.fecha.data), str(formulario.hora.data), formulario.minimo.data, formulario.maximo.data)

        elif (origen != '') and (destino != '') and (formulario.fecha.data == None) and (formulario.hora.data == None) and (formulario.minimo.data != None) and (formulario.maximo.data != None):
            objeto = Vuelos.buscarVuelos(origen, destino, None, None, formulario.minimo.data, formulario.maximo.data)

        elif (origen != '') and (destino != '') and (formulario.fecha.data == None) and (formulario.hora.data == None) and (formulario.minimo.data == None) and (formulario.maximo.data == None):
            objeto = Vuelos.buscarVuelos(origen, destino, None, None, None, None)

        elif (origen != '') and (destino == '') and (formulario.fecha.data == None) and (formulario.hora.data == None or formulario.hora.data != None) and (formulario.minimo.data == None) and (formulario.maximo.data == None):
            objeto = Vuelos.buscarVuelos(origen, None, None, None, None, None)

        elif (origen == '') and (destino != '') and (formulario.fecha.data == None) and (formulario.hora.data == None or formulario.hora.data != None) and (formulario.minimo.data == None) and (formulario.maximo.data == None):
            objeto = Vuelos.buscarVuelos(None, destino, None, None, None, None)

        elif (origen == '') and (destino == '') and (formulario.fecha.data == None) and (formulario.hora.data == None or formulario.hora.data != None) and (formulario.minimo.data == None) and (formulario.maximo.data != None):
            objeto = Vuelos.buscarVuelos(None, None, None, None, None, formulario.maximo.data)

        if objeto:
            return render_template('programar_vuelos_admin.html', form = buscarVuelos(), busqueda = objeto, destinos = listaDestinos)

        return render_template('programar_vuelos_admin.html', form = buscarVuelos(), mensaje = "no encuentra", destinos = listaDestinos)


@app.route('/reservar-vuelos', methods=['GET','POST'])
def reservar_vuelos():
    listaDestinos = Destinos.listaDestinos()
    if request.method == 'GET':
        formulario = buscarVuelos(request.form)
        return render_template('reservar_vuelos.html', form = buscarVuelos(), destinos = listaDestinos)
    elif request.method == 'POST':
        formulario = buscarVuelos(request.form)
        origen = request.form['origen']
        destino = request.form['destino']

        if (origen != '') and (destino != '') and (formulario.fecha.data != None) and (formulario.hora.data != None) and (formulario.minimo.data != None) and (formulario.maximo.data != None):
            objeto = Vuelos.buscarVuelos(origen, destino, str(formulario.fecha.data), str(formulario.hora.data), formulario.minimo.data, formulario.maximo.data)

        elif (origen != '') and (destino != '') and (formulario.fecha.data == None) and (formulario.hora.data == None) and (formulario.minimo.data != None) and (formulario.maximo.data != None):
            objeto = Vuelos.buscarVuelos(origen, destino, None, None, formulario.minimo.data, formulario.maximo.data)

        elif (origen != '') and (destino != '') and (formulario.fecha.data == None) and (formulario.hora.data == None) and (formulario.minimo.data == None) and (formulario.maximo.data == None):
            objeto = Vuelos.buscarVuelos(origen, destino, None, None, None, None)

        elif (origen != '') and (destino == '') and (formulario.fecha.data == None) and (formulario.hora.data == None or formulario.hora.data != None) and (formulario.minimo.data == None) and (formulario.maximo.data == None):
            objeto = Vuelos.buscarVuelos(origen, None, None, None, None, None)

        elif (origen == '') and (destino != '') and (formulario.fecha.data == None) and (formulario.hora.data == None or formulario.hora.data != None) and (formulario.minimo.data == None) and (formulario.maximo.data == None):
            objeto = Vuelos.buscarVuelos(None, destino, None, None, None, None)

        elif (origen == '') and (destino == '') and (formulario.fecha.data == None) and (formulario.hora.data == None or formulario.hora.data != None) and (formulario.minimo.data == None) and (formulario.maximo.data != None):
            objeto = Vuelos.buscarVuelos(None, None, None, None, None, formulario.maximo.data)

        if objeto:
            return render_template('reservar_vuelos.html', form = buscarVuelos(), busqueda = objeto, destinos = listaDestinos)

        return render_template('reservar_vuelos.html', form = buscarVuelos(), mensaje = "no encuentra", destinos = listaDestinos)
        
        #datetime.date(2021, 10, 30)
        #datetime.time(12, 0)

app.run(port = 3000, debug=True)
