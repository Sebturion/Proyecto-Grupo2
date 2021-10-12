
function validar_formulario(){
    var nombre = document.getElementById('txtNombre');
    var contacto = document.getElementById('telContacto');
    var email = document.getElementById('email');
    var contraseña = document.getElementById('password');
    var confirmar = document.getElementById('confirmPassword');
    var error1 = document.getElementById("error1");
    var error2 = document.getElementById("error2");
    var error3 = document.getElementById("error3");
    var error4 = document.getElementById("error4");
    var error5 = document.getElementById("error5");
    var hay_errores = false;

    
    error1.innerHTML = "";
    if (nombre.value.length == 0) {
        error1.innerHTML = "Ingrese su nombre y apellido";
        hay_errores = true;
    }


    error2.innerHTML = "";
    if (contacto.value.length == 0) {
        error2.innerHTML = "Ingrese su numero de contacto";
        hay_errores = true;
    }    

    
    error3.innerHTML = "";
    var formato = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if (email.value.length == 0) {
        error3.innerHTML = "Ingrese su direccion de correo electronico";
        hay_errores = true;
    } else if (!email.value.match(formato)) {
        error3.innerHTML = "Su direccion de correo no es valida"
        hay_errores = true;
    } 


    error4.innerHTML = "";
    if (contraseña.value.length == 0) {
        error4.innerHTML = "Ingrese su contraseña";
        hay_errores = true;
    }    

    
    error5.innerHTML = "";
    if (confirmar.value.length == 0) {
        error5.innerHTML = "Confirme su contraseña";
        hay_errores = true;
    }   else if (confirmar.value != contraseña.value) {
        error5.innerHTML = "Las contraseñas no coinciden";
        hay_errores = true;
    }    




    return !hay_errores;
}