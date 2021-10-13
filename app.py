from logging import debug
from flask import Flask, render_template, request

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

@app.route('/registrarse')
def registrase():
    return render_template('registrarse_usuario.html')

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
        return render_template('Comentarios_admin.html')

    return render_template('login.html')


app.run(port = 3000)
