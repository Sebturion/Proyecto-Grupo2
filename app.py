from logging import debug
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vuelos')
def vuelos():
    return render_template('vuelos.html')

@app.route('/destinos')
def destinos():
    return render_template('index.html')

@app.route('/inicio-sesion')
def login():
    return render_template('login.html')

@app.route('/registrarse', methods=['GET','POST'])
def registrarse():
    if (request.method == 'GET'):
        return render_template('registrarse_usuario.html')
    elif (request.method == 'POST'):
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        email = request.form['email']
        contraseña = request.form['contraseña']
        confirmarContraseña = request.form['confirmarContraseña']

        if len(nombre == 0) or len(contacto == 0) or len(email == 0) or len(contraseña == 0) or len(confirmarContraseña == 0):
            mensaje = "Debe completar todos los campos"
            return render_template('registrarse_usuario.html', mensaje)

        return redirect(url_for('registrarse_usuario.html'))

@app.route('/plataforma-usuario-verificar')
def plataforma_usuario_verificar():
    return render_template('plataforma_usuario_verificar.html')

@app.route('/pilotos-registrados')
def pilotos_registrados():
    return render_template('pilotos_registrados.html')

@app.route('/configuracion-plataforma_usuario')
def configuracion_plataforma_usuario():
    return render_template('configuracion_plataforma_usuario.html')

@app.route('/comentarios-admin')
def comentarios_admin():
    return render_template('comentarios_admin.html')

@app.route('/usuarios-registrados')
def usuarios_registrados():
    return render_template('usuarios_registrados.html')

@app.route('/validar-login', methods=['POST'])
def validarlogin():
    email_recibido = request.form['correo']
    contrasenia_recibida = request.form['contrasenia']

    email_admin = 'admin@gmail.com'
    contrasenia_admin = '123456'

    email_piloto = 'piloto@gmail.com'
    contrasenia_piloto = '123456'

    email_usuario_final = 'final@gmail.com'
    contrasenia_usuario_final = '123456'

    if (email_recibido == email_usuario_final and contrasenia_recibida == contrasenia_usuario_final):
        return render_template('index.html')

    if (email_recibido == email_piloto and contrasenia_recibida == contrasenia_piloto):
        return render_template('vuelos.html')

    if (email_recibido == email_admin and contrasenia_recibida == contrasenia_admin):
        return render_template('configuracion_plataforma_usuario.html')

    return render_template('login.html')


app.run(port = 3000)
