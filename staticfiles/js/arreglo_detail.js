function showAlert() {
    const alertBox = document.getElementById("mensaje");
    alertBox.classList.add("show");

    // Ocultar la alerta después de 3 segundos
    setTimeout(() => {
        alertBox.classList.remove("show");
    }, 3000); // Tiempo en milisegundos
}


const mensaje= document.getElementById("mensaje")
const a=mensaje.innerText.length;


if(a!=0){
    showAlert()
}

