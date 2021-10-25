
function validar_formulario(){
    var email = document.getElementById('email');
    var contraseña = document.getElementById('password');
    var error1 = document.getElementById("error1");
    var error2 = document.getElementById("error2");
    var hay_errores = false;

    
    error1.innerHTML = "";
    var formato = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if (email.value.length == 0) {
        error1.innerHTML = "Ingrese su direccion de correo electronico";
        hay_errores = true;
    } else if (!email.value.match(formato)) {
        error1.innerHTML = "Su direccion de correo no es valida"
        hay_errores = true;
    } 


    error2.innerHTML = "";
    if (contraseña.value.length == 0) {
        error2.innerHTML = "Ingrese su contraseña";
        hay_errores = true;
    }    

    return !hay_errores;
}