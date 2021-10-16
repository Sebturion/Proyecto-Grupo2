from logging import debug
from flask import Flask, render_template, request, redirect, url_for
from forms import formularioLogin, formularioRegistro
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/vuelos', methods=['GET'])
def vuelos():
    return render_template('vuelos.html')

@app.route('/destinos', methods=['GET'])
def destinos():
    return render_template('destinos.html')


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
                return redirect(url_for('index'))

            if (email_recibido == email_piloto and contrasenia_recibida == contrasenia_piloto):
                return redirect(url_for('vuelos'))

            if (email_recibido == email_admin and contrasenia_recibida == contrasenia_admin):
                return redirect(url_for('configuracion_plataforma_usuario'))
 

@app.route('/registrarse', methods=['GET','POST'])
def registrarse():
    error = False
    formulario = formularioRegistro(request.form)

    if formulario.confirmar.data != formulario.contrasena.data:
        error = True

    if request.method == 'GET':
        return render_template("registrarse_usuario.html", form = formularioRegistro())
    elif request.method == 'POST':
        if (formulario.validate_on_submit()) and (not error):
            mensaje = "Registro exitoso"
            return render_template("registrarse_usuario.html", form = formularioRegistro(), mensaje = mensaje)
        
        mensaje = "No se ha podido realizar el registro"
        return render_template("registrarse_usuario.html", form = formularioRegistro(), mensaje = mensaje)



@app.route('/plataforma-usuario-verificar', methods=['GET'])
def plataforma_usuario_verificar():
    return render_template('plataforma_usuario_verificar.html')

@app.route('/pilotos-registrados', methods=['GET'])
def pilotos_registrados():
    return render_template('pilotos_registrados.html')

@app.route('/configuracion-plataforma_usuario', methods=['GET'])
def configuracion_plataforma_usuario():
    return render_template('configuracion_plataforma_usuario.html')

@app.route('/comentarios-admin', methods=['GET'])
def comentarios_admin():
    return render_template('comentarios_admin.html')

@app.route('/usuarios-registrados', methods=['GET'])
def usuarios_registrados():
    return render_template('usuarios_registrados.html')




app.run(port = 3000)
