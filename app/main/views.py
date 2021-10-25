from flask import render_template

# import the main blue print instance
from app.main import main

@main.route('/')
def index():
    return render_template('index.html')


# @vuelos.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')



# @vuelos.route('/vuelos', methods=['GET', 'POST'])
# def vuelos():
#     if (request.method == 'GET'):
#         objeto = Vuelos.mostarVuelos(None)
#         if objeto:
#             return render_template('vuelos.html', vuelos = objeto)
#         else:
#             return render_template('vuelos.html', mensaje = "En este momento no hay ofertas de vuelos.")
#     elif (request.method == 'POST'):
#         lugar = request.form['txtBuscador']
#         objeto = Vuelos.mostarVuelos(lugar)
#         if objeto:
#             return render_template('vuelos.html', vuelos = objeto)
#         else:
#             return render_template('vuelos.html', mensaje = ("En este momento no hay ofertas de vuelos a " + lugar))



# @vuelos.route('/destinos', methods=['GET', 'POST'])
# def destinos():
#     if (request.method == 'GET'):
#         objeto = Destinos.mostrarDestinos(None)
#         if objeto:
#             return render_template('destinos.html', destinos = objeto)
#         else:
#             return render_template('destinos.html', mensaje = "En este momento no destinos disponibles.")
#     elif (request.method == 'POST'):
#         destino = request.form['txtBuscador']
#         objeto = Destinos.mostrarDestinos(destino)
#         if objeto:
#             return render_template('vuelos.html', destinos = objeto)
#         else:
#             return render_template('vuelos.html', mensaje = ("No se encontró el destino que desea"))



# @vuelos.route('/registrarse', methods=['GET','POST'])
# def registrarse():
#     if request.method == 'GET':
#         return render_template("registrarse_usuario.html", form = formularioRegistro())
#     elif request.method == 'POST':
#         formulario = formularioRegistro(request.form)
        
#         error = False
#         if formulario.confirmar.data != formulario.contrasena.data:
#             error = True

#         if (formulario.validate_on_submit()) and (not error):
#             nuevoUsuario = Usuario(formulario.nombreApellido.data, formulario.numeroContacto.data, formulario.correo.data, formulario.contrasena.data)
#             if nuevoUsuario.insert():
#                 return render_template("registrarse_usuario.html", form = formularioRegistro(), mensaje = "Registro exitoso")
#             else:
#                 return render_template("registrarse_usuario.html", form = formularioRegistro(), mensaje = "Registro fallido. Consulte con soporte tecnico")
        
#         return render_template("registrarse_usuario.html", form = formulario, mensaje = "Registro fallido")



# @vuelos.route('/plataforma-usuario-verificar', methods=['GET'])
# def plataforma_usuario_verificar():
#     return render_template('plataforma_usuario_verificar.html')

# @vuelos.route('/pilotos-registrados', methods=['GET'])
# def pilotos_registrados():
#     return render_template('pilotos_registrados.html')

# @vuelos.route('/configuracion-plataforma_usuario', methods=['GET'])
# def configuracion_plataforma_usuario():
#     return render_template('configuracion_plataforma_usuario.html')

# @vuelos.route('/comentarios-admin', methods=['GET'])
# def comentarios_admin():
#     return render_template('comentarios_admin.html')

# @vuelos.route('/usuarios-registrados', methods=['GET'])
# def usuarios_registrados():
#     return render_template('usuarios_registrados.html')


