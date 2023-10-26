//selcciona los id de div principales
const aspectDiv = document.getElementById("Aspect");
const ubicationDiv = document.getElementById("Ubication");
const dateDiv = document.getElementById("Date");
const organizationDiv = document.getElementById("Organization");
const dirigentDiv = document.getElementById("Dirigent");
const measurementTypeDiv = document.getElementById("MeasurementType");  
 // Selecciona todos los elementos con la clase "ItemFields"
const _ItemFields = document.querySelectorAll(".ItemFields");

// Itera a través de los elementos y asigna un controlador de eventos
_ItemFields.forEach((elemento) => {
    _ItemFields[0].style.backgroundColor="rgb(250, 109, 109)"
  elemento.addEventListener("click", () => {
    // Obtiene el valor del elemento y lo escribe en la consola
    const valor = elemento.textContent;
    _ItemFields.forEach((el) =>{
        el.style.backgroundColor="#85E6C5"
    })
    elemento.style.backgroundColor = "rgb(250, 109, 109)"
    switch (valor) {
      case "Aspecto":
        aspectDiv.style.display="flex";
        ubicationDiv.style.display="none"
        dateDiv.style.display="none"
        organizationDiv.style.display="none"
        dirigentDiv.style.display="none"
        measurementTypeDiv.style.display="none"
        break;
      case "Ubicacion":
        aspectDiv.style.display="none";
        ubicationDiv.style.display="flex"
        dateDiv.style.display="none"
        organizationDiv.style.display="none"
        dirigentDiv.style.display="none"
        measurementTypeDiv.style.display="none"
        break;
      case "Fecha":
        aspectDiv.style.display="none";
        ubicationDiv.style.display="none"
        dateDiv.style.display="flex"
        organizationDiv.style.display="none"
        dirigentDiv.style.display="none"
        measurementTypeDiv.style.display="none"
        break;
      case "Organizacion":
        aspectDiv.style.display="none";
        ubicationDiv.style.display="none"
        dateDiv.style.display="none"
        organizationDiv.style.display="flex"
        dirigentDiv.style.display="none"
        measurementTypeDiv.style.display="none"
        break;
      case "Dirigente":
        aspectDiv.style.display="none";
        ubicationDiv.style.display="none"
        dateDiv.style.display="none"
        organizationDiv.style.display="none"
        dirigentDiv.style.display="flex"
        measurementTypeDiv.style.display="none"
        break;
      case "Tipo de medida":
        aspectDiv.style.display="none";
        ubicationDiv.style.display="none"
        dateDiv.style.display="none"
        organizationDiv.style.display="none"
        dirigentDiv.style.display="none"
        measurementTypeDiv.style.display="flex"
        break;
      default:
        console.log("Opción no válida");
    }
  });
});