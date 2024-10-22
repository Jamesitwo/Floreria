#necesario importar para redireccionar y enviar html
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from .forms import crearPedido
import random
from datetime import datetime
# Create your views here.
def index(request):
    Arreglos=list(arreglos.objects.all())
    arreglos_random= random.sample(Arreglos, 5)
    return render(request,"index.html",{
        "Arreglos":arreglos_random
    })
    

def contacto(request):
    return render(request,"contacto.html")


# def Categorias(request):
#     a=categorias.objects.values()
#     a=list(a)
#     return JsonResponse(a,safe=False)


def Arreglos(request):
    
    print("entro en arreglos")
    Arreglos=list(arreglos.objects.all())
    return render(request,"arreglos.html",{
        "Arreglos":Arreglos
    })

def crear_pedido(request, id):
    print(id)
    if request.method=="GET":
        return render(request,"crear_pedidos.html",{
        "formulario":crearPedido()
    }) 
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
            muicipio=request.POST["muicipio"],
            barrio=request.POST["barrio"],
            celularR=request.POST["celularR"],
            quienEnvia=request.POST["quienEnvia"],
            fechaenvio=datetime.strptime(fechaenvio_str, '%Y-%m-%dT%H:%M'),
            mensaje=request.POST["mensaje"],
            arreglo= arreglos.objects.get(id=id))
        if (metodoP=="valor1"):
            return redirect("https://www.pse.com.co/persona")
        else:
            return redirect("https://www.paypal.com/co/home")
            

        
    
# def verpedido(request):
#     pedidos=list(Pedido.objects.all())
#     return render(request,"pedido.html",{
#         "pedidos":pedidos
#     })

def arreglo(request,id):

    arreglo_detail=arreglos.objects.get(id=id)
    Arreglos=list(arreglos.objects.all())
    arreglos_random= random.sample(Arreglos, 5)
    return render(request,"arreglo.html", {
        "arreglo":arreglo_detail,
        "Arreglos":arreglos_random
    })
    

