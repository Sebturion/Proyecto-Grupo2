import re
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import IntegerField, StringField
from wtforms import validators
from wtforms.fields.simple import PasswordField, SubmitField


class formularioRegistro(FlaskForm):

    nombreApellido = StringField(validators=[validators.required(), validators.length(max=30)])
    numeroContacto = IntegerField(validators=[validators.required()])
    correo = StringField(validators=[validators.required(), validators.Email(), validators.length(max=50)])
    contrasena = PasswordField(validators=[validators.required(), validators.length(max=20)])
    confirmar = PasswordField(validators=[validators.required(), validators.length(max=20)])
    registrarse = SubmitField('Registrarse')


class formularioLogin(FlaskForm):
    correo = StringField(validators=[validators.required(), validators.Email(), validators.length(max=50)])
    contrasena = PasswordField(validators=[validators.required(), validators.length(max=20)])
    login = SubmitField('Iniciar Sesión')