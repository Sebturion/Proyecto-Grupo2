const rango = document.querySelector("#rango");
const valor = document.querySelector("#valor");
const minvalue = document.querySelector("#minvalue");
const maxvalue = document.querySelector("#maxvalue");
            
            
rango.oninput = () => {
    valor.innerHTML = "$" + rango.value
}