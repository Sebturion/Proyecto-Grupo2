import re
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import IntegerField, StringField
from wtforms import validators, ValidationError
from wtforms.fields.simple import PasswordField, SubmitField


class formularioRegistro(FlaskForm):

    nombreApellido = StringField(validators=[validators.DataRequired(message="Ingrese su nombre y apellido"), validators.length(max=30)])
    numeroContacto = IntegerField(validators=[validators.DataRequired(message="Ingrese su numero de contacto")])
    correo = StringField(validators=[validators.DataRequired(message="Ingrese su correo"), validators.Email(), validators.length(max=50)])
    contrasena = PasswordField(validators=[validators.DataRequired(message="Ingrese una contraseña"), validators.length(max=20)])
    confirmar = PasswordField(validators=[validators.DataRequired(message="Confirme su contraseña"), validators.length(max=20), validators.EqualTo('contrasena', message='Son diferentes')])
    registrarse = SubmitField('Registrarse')


class formularioLogin(FlaskForm):
    correo = StringField(validators=[validators.required(), validators.Email(), validators.length(max=50)])
    contrasena = PasswordField(validators=[validators.required(), validators.length(max=20)])
    login = SubmitField('Iniciar Sesión')