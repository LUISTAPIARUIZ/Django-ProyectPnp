document.addEventListener("DOMContentLoaded", function () {
    var formulario = document.getElementById("FormGremio");

    formulario.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío del formulario por defecto

        let formData = new FormData(formulario);
        let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        let xhr = new XMLHttpRequest();
        xhr.open("POST", formulario.action, true);
        xhr.setRequestHeader("X-CSRFToken", csrfToken); // Agregar el token CSRF a la solicitud
        xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    // Manejar la respuesta del servidor
                    let response = JSON.parse(xhr.responseText);
                    console.log(response.message)
                    if (response.message === 'Registro exitoso') {
                        mostrarMensajeEmergente(response.message,"success");
                        formulario.reset();
                    }
                    if (response.message === 'Error en el formato') {
                        mostrarMensajeEmergente(response.message,"danger");
                    }
                }
                if (xhr.readyState === 4 && xhr.status !== 200) {
                    // Manejar la respuesta del servidor
                    mostrarMensajeEmergente("Up! ocurrio un error","Erro de servidor");
                }
        };

        xhr.send(formData);
    });
    function mostrarMensajeEmergente(mensaje,tipo) {
        if(tipo=="success"){
            let mensajeDiv = document.getElementById("message_success");
            mensajeDiv.textContent=mensaje
            mensajeDiv .classList.remove("hide");

            setTimeout(function () {
                mensajeDiv.classList.add("hide");
            }, 3000); // Desaparecer después de 3 segundos
            }
        if(tipo=="danger"){
            let mensajeDiv = document.getElementById("alert-danger");
            mensajeDiv.textContent=mensaje
            mensajeDiv .classList.remove("hide");

            setTimeout(function () {
                mensajeDiv.classList.add("hide");
            }, 3000); // Desaparecer después de 3 segundos
            }
        if(tipo=="Erro de servidor"){
            let mensajeDiv = document.getElementById("alert-danger");
            mensajeDiv.textContent=mensaje
            mensajeDiv .classList.remove("hide");

            setTimeout(function () {
                mensajeDiv.classList.add("hide");
            }, 3000); // Desaparecer después de 3 segundos
            }
    }
});