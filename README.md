# Proyecto-Grupo2

Proyecto inicial de Uncontrolled Airport.

En el momento tenemos pendientes los siguientes temas:
1. Finalizar el diseño de la base de datos: https://lucid.app/lucidchart/b6cd8320-395e-4b93-b8fc-64e07a0f788a/edit?invitationId=inv_f29f872c-6b65-4ed9-a154-da1e96b3480f
2. Diseñar y crear cada uno de los mockups presentados en el Sprint2: https://drive.google.com/file/d/1S9BqcAnpyT_OjMm-g9fEb15c0LCAqNq2/view?usp=sharing
3. Comenzar con el Backend y definir todo el manejo de información
4. Creación de API ?

## TODO DEBE ESTAR DESACOPLADO: https://www.aunitz.net/aplicaciones-web-front-end-back-end-desacoplado/

Especificacion manejadores 
==============
| URL | Metodo HTTP  | Parametros  | Funcionalidad |
| ------- | --- | --- | --- |
| /validar-login | POST | [correo, contrasenia] | Valida si el usuario es valido y si es un super usuario, usuario final o piloto |
| /registrarse | POST | [nombre,telefono,correo, contrasenia,confirmarContrasenia] | Valida que los datos ingresados no esten vacios y registra un nuevo usuario final |
| /registrarse | GET |  | Muestra la pantalla de creacion de usuarios finales |


## RUN MIGRATIONS

