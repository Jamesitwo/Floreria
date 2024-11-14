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
const mensaje2= document.getElementById("mensaje2")
const b=mensaje2.innerText.length;
const imagen_carrito=document.getElementById("imagen_carrito")
const mensaje_box=document.getElementById("mensaje_box")
console.log("b")
if(b==0){
    imagen_carrito.style.display = "none";
    mensaje_box.style.display="none"
}else{
    imagen_carrito.style.display = "visible";
}

if(a!=0){
    showAlert()
}
