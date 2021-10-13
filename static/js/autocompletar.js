 var IDs = ["Juan Antonio Ramirez", "Juan Antonio Bermudez", "Jesus David Nuñez", "Jorge Antonio Salazar", "Andres Danilo Rodriguez", "Antonio David Diaz"];

 function autocomplete(inp, arr) {
    /* la función de autocompletar toma dos argumentos,
    el elemento del campo de texto y un array de posibles valores autocompletados: */ 
    var currentFocus;
    /*ejecutar una función cuando alguien escribe en el campo de texto: */     
        inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*cerrar cualquier lista abierta de valores autocompletados*/ 
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*crea un elemento DIV que contendrá los elementos (valores): */        
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*agregar el elemento DIV como un elemento secundario del contenedor de autocompletar:*/ 
        this.parentNode.appendChild(a);
        /*for each item en el array...*/
        for (i = 0; i < arr.length; i++) {
          /*comprobar si el elemento comienza con las mismas letras que el valor del campo de texto:*/ 
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*crea un elemento DIV para cada elemento coincidente:*/ 
            b = document.createElement("DIV");
            /*poner las letras correspondientes en negrita: */ 
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            /*inserta un input de entrada que contendrá el valor del elemento de la matriz actual: */ 
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            /*ejecutar una función cuando alguien hace clic en el valor del artículo (elemento DIV): */ 
                b.addEventListener("click", function(e) {
                /*inserta el valor para el campo de texto de autocompletar: */ 
                inp.value = this.getElementsByTagName("input")[0].value;
                /*cerrar la lista de valores de autocompletar, 
                (o cualquier otra lista abierta de valores de autocompletar: */ 
                closeAllLists();
            });
            a.appendChild(b);
          }
        }
    });
    /*ejecutar una función presiona una tecla en el teclado: */ 
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
          /* Si se presiona la tecla de flecha ABAJO,
           aumentar la variable currentFocus: */ 
          currentFocus++;
          /* hacer que el elemento actual sea más visible: */ 
          addActive(x);
        } else if (e.keyCode == 38) { //up
          /* Si se presiona la tecla de flecha ARRIBA,
           disminuir la variable currentFocus: */ 
          currentFocus--;
          /* y hacer que el elemento actual sea más visible: */ 
          addActive(x);
        } else if (e.keyCode == 13) {
          /* Si se presiona la tecla ENTER, evitar que se envíe el formulario, */ 
          e.preventDefault();
          if (currentFocus > -1) {
            /* y simular un clic en el elemento "activo": */ 
            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {
      /* una función para clasificar un elemento como "activo": */ 
      if (!x) return false;
      /* comienza eliminando la clase "activa" en todos los elementos: */
      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      /* Agregar clase "autocomplete-active":*/
      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
      /* una función para eliminar la clase "active" de todos los elementos de autocompletar: */
      for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      /* cerrar todas las listas de autocompletar en el documento,
       excepto el pasado como argumento: */ 
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /* ejecutar una función cuando alguien hace clic en el documento: */ 
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
  }

  autocomplete(document.getElementById("myInput"), IDs);
