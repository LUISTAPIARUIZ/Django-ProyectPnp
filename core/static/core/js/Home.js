// Obtener referencias a los botones
let btnBuscarEvento = document.getElementById("btnBuscarEvento");
let btnBuscarGremio = document.getElementById("btnBuscarGremio");
let btnBuscarPersona = document.getElementById("btnBuscarPersona");

function hacerPeticionGETConToken(url, token, callback) {
    let xhr = new XMLHttpRequest();

    // Configurar la solicitud GET
    xhr.open('GET', url, true);

    // Configurar el encabezado de autorización con el token
    xhr.setRequestHeader('Authorization', 'Token ' + token);

    // Configurar el manejo de la respuesta
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // La solicitud GET fue exitosa
                callback(null, xhr.responseText);
            } else {
                // Hubo un error en la solicitud GET
                callback(new Error(`Error en la solicitud GET: ${xhr.status}`));
            }
        }
    };

    // Enviar la solicitud GET
    xhr.send();
}
let url = 'http://127.0.0.1:8000/home';
let authToken = 'tu_token_aqui';
function gestionarError(error, respuesta){
    if (error) {
        console.log('hola');
    } else {
        console.log('Respuesta exitosa:', respuesta);
        // Aquí puedes manejar la respuesta de la solicitud GET con token
    }
}
;
// Agregar event listener a cada botón
btnBuscarEvento.addEventListener("click", hacerPeticionGETConToken.bind(null, url, authToken, gestionarError));
btnBuscarGremio.addEventListener("click", hacerPeticionGETConToken.bind(null, url, authToken, gestionarError));
btnBuscarPersona.addEventListener("click", hacerPeticionGETConToken.bind(null, url, authToken, gestionarError));