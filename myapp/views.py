#necesario importar para redireccionar y enviar html
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from .forms import crearPedido
import random
from datetime import datetime
from .carritoCompras import *
# Create your views here.

def index(request):
    Arreglos=list(Arreglo.objects.all())
    arreglos_random= random.sample(Arreglos, 5)
    return render(request,"index.html",{
        "Arreglos":arreglos_random
    })
    

def contacto(request):
    return render(request,"contacto.html")



def Arreglos(request):
    
    print("entro en arreglos")
    Arreglos=list(Arreglo.objects.all())
    return render(request,"arreglos.html",{
        "Arreglos":Arreglos
    })

def crear_pedido(request, id):
    print(id)
    if request.method=="GET":
        return render(request,"crear_pedidos.html") 
    else:
        metodoP=request.POST["metodoP"]
        print(metodoP)
        fechaenvio_str = request.POST["fechaenvio"]
        
       # fechaenvio = datetime.strptime(fechaenvio_str, '%Y-%m-%dT%H:%M')
        #arreglo_instance =
        Pedido.objects.create(
            nombre=request.POST["nombre"],
            email=request.POST["email"],
            cedula=request.POST["cedula"],
            celular=request.POST["celular"],
            nombreR=request.POST["nombreR"],
            direccion=request.POST["direccion"],
            muicipio=request.POST["municipio"],
            barrio=request.POST["barrio"],
            celularR=request.POST["celularR"],
            quienEnvia=request.POST["quienEnvia"],
            fechaenvio=datetime.strptime(fechaenvio_str, '%Y-%m-%dT%H:%M'),
            mensaje=request.POST["mensaje"])
        if (metodoP=="valor1"):
            return redirect("https://www.pse.com.co/persona")
        else:
            return redirect("https://www.paypal.com/co/home")
            
#-----------------------------------------------------------------------
def arreglo_detalle(request,id):

#Toma el id del del arreglo en especifico para enviarlo al html
    arreglo_detail=Arreglo.objects.get(id=id)
#Vista de los arreglos de la parte inferior
    Arreglos=list(Arreglo.objects.all())
    arreglos_random= random.sample(Arreglos, 5)
   

    if request.method=="POST":
        a=comprobar_stock(arreglo_detail,1)
        pass


    return render(request,"arreglo.html", {
        "arreglo":arreglo_detail,
        "Arreglos":arreglos_random,
        
        
    })
    


def carrito(request):
    total=calcularTotales()
    if(request.method=="POST"):
        id=request.POST["id"]
        arreglo=Arreglo.objects.get(id=id)
        accion= request.POST.get("opcion")
        if(accion=="mas"):
            comprobar_stock(arreglo,1)
        elif(accion=="menos"):
            comprobar_stock(arreglo,-1)
            pass
        elif(accion=="eliminar"):
            eleminarCarrito(arreglo)
            
        total=calcularTotales()


    cantidad_y_arreglo=list(zip(arreglosComprar,arreglosCantidades,totalValorArreglo))
    print(cantidad_y_arreglo)
    return render(request, "carrito.html",{
        "cantidad_y_arreglo":cantidad_y_arreglo,
        "total":total,
        "zip":zip
    })