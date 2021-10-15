from logging import debug
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
    if (request.method == 'POST'):
        email_recibido = request.form['correo']
        contrasenia_recibida = request.form['contrasenia']

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
 
    return render_template('login.html')


@app.route('/registrarse', methods=['GET','POST'])
def registrarse():
    if (request.method == 'POST'):
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        email = request.form['correo']
        contrasenia = request.form['contrasenia']
        confirmarContrasenia = request.form['confirmarContrasenia']

        if len(nombre) == 0 or len(contacto) == 0 or len(email) == 0 or len(contrasenia) == 0 or len(confirmarContrasenia) == 0 :
            return render_template('registrarse_usuario.html', mensaje = "Debe completar todos los campos")
        return render_template("registrarse_usuario.html", mensaje = "Usuario creado exitosamente")

    return render_template("registrarse_usuario.html")

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
