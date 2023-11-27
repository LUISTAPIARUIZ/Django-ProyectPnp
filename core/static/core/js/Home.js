// Obtener referencias a los botones
let btnEvento = document.getElementById("btnBuscarEvento");
let btnGremio = document.getElementById("btnBuscarGremio");
let btnPersona = document.getElementById("btnBuscarPersona");
let inputOpcionBuscar = document.getElementById("OpcionSearch");

let formBuscar = document.getElementById("buscador");


let tablehead =document.getElementById("head")
let tablebody =document.getElementById("body")

let urlGremio = 'http://127.0.0.1:8000/obtenerGremio/';
let urlPersona = 'http://127.0.0.1:8000/obtenerPersona/';
let urlEvento = 'http://127.0.0.1:8000/obtenerEvento/';

let authToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
hacerPeticionGETConToken(urlEvento, authToken)

formBuscar.addEventListener("submit", function (event) {
    event.preventDefault(); // Evita el envío del formulario por defecto

    let formData = new FormData(formBuscar);
    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    let xhr = new XMLHttpRequest();
    xhr.open("POST", formBuscar.action, true);
    xhr.setRequestHeader("X-CSRFToken", csrfToken); // Agregar el token CSRF a la solicitud
    xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Manejar la respuesta del servidor
                let response = JSON.parse(xhr.responseText);
                crearFilasEnTabla(response.resultados)

            }
            if (xhr.readyState === 4 && xhr.status !== 200) {
                // Manejar la respuesta del servidor
                console.log('error')
            }
    };

    xhr.send(formData);
});

function hacerPeticionGETConToken(url, token) {
    let xhr = new XMLHttpRequest();

    // Configurar la solicitud GET
    xhr.open('GET', url, true);

    // Configurar el encabezado de autorización con el token
    xhr.setRequestHeader('Authorization', 'Token ' + token);

    // Configurar el manejo de la respuesta
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                let respuestaJSON = JSON.parse(xhr.responseText);

                if (respuestaJSON && respuestaJSON.registro && respuestaJSON.Opcion) {
                    if(respuestaJSON.Opcion =="gremio"){
                        btnGremio.style.backgroundColor = "#1d1b31";
                        btnEvento.style.backgroundColor = "white";
                        btnPersona.style.backgroundColor = "white";
                        btnEvento.style.color = "black";
                        btnGremio.style.color = "white";
                        btnPersona.style.color = "black";
                        inputOpcionBuscar.value="Gremio";
                        imprimirClaves(respuestaJSON.registro)
                        crearFilasEnTabla(respuestaJSON.registro)
                    }
                    if(respuestaJSON.Opcion =="persona"){
                        btnGremio.style.backgroundColor = "white";
                        btnEvento.style.backgroundColor = "white";
                        btnPersona.style.backgroundColor = "#1d1b31";
                        btnEvento.style.color = "black";
                        btnGremio.style.color = "black";
                        btnPersona.style.color = "white";
                        inputOpcionBuscar.value="Persona";
                        imprimirClaves(respuestaJSON.registro)
                        crearFilasEnTabla(respuestaJSON.registro)
                    }
                    if(respuestaJSON.Opcion =="evento"){
                        btnGremio.style.backgroundColor = "white";
                        btnEvento.style.backgroundColor = "#1d1b31";
                        btnPersona.style.backgroundColor = "white";
                        btnEvento.style.color = "white";
                        btnGremio.style.color = "black";
                        btnPersona.style.color = "black";
                        inputOpcionBuscar.value="Evento";
                        imprimirClaves(respuestaJSON.registro)
                        crearFilasEnTabla(respuestaJSON.registro)
                    }
                } else {
                    resultadoElement.textContent = 'Respuesta inesperada';
                }
            } else {
                console.log('invalido')
            }
        }
    };

    // Enviar la solicitud GET
    xhr.send();
}
function crearFilasEnTabla(jsonArray) {
    // Limpiar el contenido actual del tbody
    tablebody.innerHTML = "";

    // Iterar sobre cada objeto en el arreglo
    jsonArray.forEach(function(json) {
        // Crear un elemento tr para cada objeto
        let tr = document.createElement("tr");

        // Iterar sobre las claves del objeto
        for (let key in json) {
            if (json.hasOwnProperty(key)) {
                // Crear un elemento td para cada par clave-valor
                let td = document.createElement("td");
                td.textContent = json[key];

                // Agregar el td al tr
                tr.appendChild(td);
            }
        }

        // Agregar el tr al tbody
        tablebody.appendChild(tr);
    });
}

function imprimirClaves(json) {
    // Obtener el primer key
    var primerKey = Object.keys(json)[0];

    // Verificar que el valor asociado al primer key sea un objeto
    if (typeof json[primerKey] === 'object' && json[primerKey] !== null) {
        tablehead.innerHTML = "";
        let trHead = document.createElement("tr");
        // Imprimir las claves del objeto anidado en la consola
        let objetoAnidado = json[primerKey];

        for (var key in objetoAnidado) {
            if (objetoAnidado.hasOwnProperty(key)) {
                let th = document.createElement("th");
                th.textContent = key;

                // Agregar el th al tr
                trHead .appendChild(th);
            }
        }
        tablehead.appendChild(trHead);
    } else {
        console.log("El valor asociado al primer key no es un objeto.");
    }
}
// Agregar event listener a cada botón
btnEvento.addEventListener("click", hacerPeticionGETConToken.bind(null, urlEvento, authToken));
btnGremio.addEventListener("click", hacerPeticionGETConToken.bind(null, urlGremio, authToken));
btnPersona.addEventListener("click", hacerPeticionGETConToken.bind(null, urlPersona, authToken));