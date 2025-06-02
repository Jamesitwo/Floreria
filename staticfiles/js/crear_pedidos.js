function contieneLetras(str){
    const A_Z=/[a-zA-z]/;
    return A_Z.test(str);
}

function eleminarLetras(str){
    return str.slice(0,-1);
}


const Cedula= document.getElementById("cedula");
const Telefono=document.getElementById("celular")
const TelefonoR=document.getElementById("celularR")

Cedula.addEventListener("input",()=>{
    if(contieneLetras(Cedula.value)){
        Cedula.value=eleminarLetras(Cedula.value)
        //alert("number")
    }

})

celularR.addEventListener("input",()=>{
    if(contieneLetras(celularR.value)){
        celularR.value=eleminarLetras(celularR.value)
        //alert("number")
    }

})

Telefono.addEventListener("input",()=>{
    if(contieneLetras(Telefono.value)){
        Telefono.value=eleminarLetras(Telefono.value)
        //alert("number")
    }

})

let currentStep = 0;
const steps = document.querySelectorAll(".form-step");

function showStep(step) {
    steps.forEach((el, index) => {
        el.classList.toggle("active", index === step);
    });
}

function nextStep() {
    if (currentStep < steps.length - 1) {
        currentStep++;
        showStep(currentStep);
    }
}

function prevStep() {
    if (currentStep > 0) {
        currentStep--;
        showStep(currentStep);
    }
}


document.addEventListener("DOMContentLoaded", function () {
    const formStep1 = document.querySelector(".form-step.active"); // Primera sección del formulario
    const nextButton = document.getElementById("Btn_siguiente"); // Botón "Siguiente"
    const submitButton = document.querySelector("button[name='proceder_pago']"); // Botón "Proceder al pago"
    const formStep2 = document.querySelectorAll(".form-step")[1]; // Segunda sección del formulario

    // Función para verificar si todos los campos de una sección están llenos
    function checkFieldsInSection(section) {
        const inputs = section.querySelectorAll("input[required], textarea[required], select[required]");
        return Array.from(inputs).every(input => input.value.trim() !== "");
    }

    // Función para actualizar el estado del botón "Siguiente"
    function updateNextButton() {
        nextButton.disabled = !checkFieldsInSection(formStep1); // Habilita el botón si todos los campos están llenos
    }

    // Función para actualizar el estado del botón "Proceder al pago"
    function updateSubmitButton() {
        submitButton.disabled = !checkFieldsInSection(formStep2); // Habilita el botón si todos los campos están llenos
    }

    // Agregar eventos de escucha para la primera sección
    const inputsStep1 = formStep1.querySelectorAll("input[required]");
    inputsStep1.forEach(input => {
        input.addEventListener("input", updateNextButton);
    });

    // Agregar eventos de escucha para la segunda sección
    const inputsStep2 = formStep2.querySelectorAll("input[required], textarea[required], select[required]");
    inputsStep2.forEach(input => {
        input.addEventListener("input", updateSubmitButton);
    });

    // Llamar a las funciones de verificación al cargar la página
    updateNextButton();
    updateSubmitButton();
});

