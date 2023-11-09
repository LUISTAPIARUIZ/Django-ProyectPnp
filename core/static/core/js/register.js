//selcciona los id de div principales de la lista de registros
const _R_events = document.getElementById("R-Events");
const _R_gremio = document.getElementById("R-Gremio");
const _R_person = document.getElementById("R-Person");
const _R_cuadros = document.getElementById("R-Cuadros");
 // Selecciona todos los elementos con la clase "ItemRegister"
const _ItemRegister = document.querySelectorAll(".ItemRegister");
_ItemRegister[0].style.textDecoration = "underline";
//selcciona los id de div principales de RegistrarEventos
const aspectDiv = document.getElementById("Aspect");
const ubicationDiv = document.getElementById("Ubication");
const dateDiv = document.getElementById("Date");
const organizationDiv = document.getElementById("Organization");
const dirigentDiv = document.getElementById("Dirigent");
const measurementTypeDiv = document.getElementById("MeasurementType");  
 // Selecciona todos los elementos con la clase "ItemFields"
const _ItemFields = document.querySelectorAll(".ItemFields");
_ItemFields[0].style.backgroundColor="rgb(250, 109, 109)"





_ItemRegister.forEach((elemento)=>{
  elemento.addEventListener("click", () =>{
    _ItemRegister.forEach((el)=>{
      el.style.textDecoration="none"
    });
    elemento.style.textDecoration="underline";
    const datoRegistro=  elemento.textContent;
    switch (datoRegistro) {
      case "Registrar evento":
        _R_events.style.display="block"
        _R_gremio.style.display="none"
        _R_person.style.display="none"
        _R_cuadros.style.display="none"
        break;
      case "Registrar Gremio":
        _R_events.style.display="none"
        _R_gremio.style.display="block"
        _R_person.style.display="none"
        _R_cuadros.style.display="none"
        break;
      case "Registrar Persona":
        _R_events.style.display="none"
        _R_gremio.style.display="none"
        _R_person.style.display="block"
        _R_cuadros.style.display="none"
        break;
      case "Registrar Cuadros":
        _R_events.style.display="none"
        _R_gremio.style.display="none"
        _R_person.style.display="none"
        _R_cuadros.style.display="block"
        break;
      default:
        console.log("Opción no válida");
    }
  })
})
// Itera a través de los elementos y asigna un controlador de eventos
_ItemFields.forEach((elemento) => {
   
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