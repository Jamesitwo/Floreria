#necesario importar para redireccionar y enviar html
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from .forms import crearPedido
import random
from datetime import datetime
from .carritoCompras import *
from django.contrib.auth import get_user_model
from django.http import HttpResponse
# Create your views here.

categorias=Categoria.objects.all()
def index(request):
    
    #base(request)
    Arreglos=list(Arreglo.objects.filter(stock__gt=0))
    #arreglos_random= random.sample(Arreglos, 5)
    return render(request,"index.html",{
        "Arreglos":Arreglos,
        "categorias":categorias,
    })
    

def contacto(request):
    return render(request,"contacto.html",{
        "categorias":categorias,
    })



def Arreglos(request,categoria):
    Arreglos=list(Arreglo.objects.filter(stock__gt=0))
    print("entro en arreglos")
    if not(categoria=="todos"):
        categoria=Categoria.objects.get(nombre=categoria)
        Arreglos=list(Arreglo.objects.filter(stock__gt=0, categorias=categoria))
        pass

    
    return render(request,"arreglos.html",{
        "Arreglos":Arreglos,
        "categorias":categorias,
    })

def crear_pedido(request):
    total=calcularTotales()
    if(len(arreglosComprar)==0):
        return redirect("/arreglos/todos")
        
    if(request.method=="POST"):
        print("crear pedido")
        
        fechaenvio_str = request.POST["fechaenvio"]
        pedido=Pedido(
            nombre=request.POST["nombre"],
            email=request.POST["email"],
            cedula=request.POST["cedula"],
            celular=request.POST["celular"],
            nombreR=request.POST["nombreR"],
            direccion=request.POST["direccion"],
            municipio=request.POST["municipio"],
            barrio=request.POST["barrio"],
            celularR=request.POST["celularR"],
            quienEnvia=request.POST["quienEnvia"],
            fechaenvio=datetime.strptime(fechaenvio_str, '%Y-%m-%dT%H:%M'),
            mensaje=request.POST["mensaje"],
            total_pagado=total
        )
        guardarBD(pedido)
        return redirect("/")

        pass
    cantidad_y_arreglo=list(zip(arreglosComprar,arreglosCantidades,totalValorArreglo))
    
    return render(request,"crear_pedidos.html",{
        "cantidad_y_arreglo":cantidad_y_arreglo,
        "total":total,
        "categorias":categorias,

    })
#-----------------------------------------------------------------------
def arreglo_detalle(request,nombre):

#Toma el id del del arreglo en especifico para enviarlo al html
    arreglo_detail=Arreglo.objects.get(nombre=nombre)
#Vista de los arreglos de la parte inferior
    Arreglos=list(Arreglo.objects.filter(stock__gt=0))
    #arreglos_random= random.sample(Arreglos, 5)
    mensaje=""

    if request.method=="POST":
        arreglo=Arreglo.objects.get(nombre=nombre)
        agregar_comprar=request.POST.get("agregar_comprar")
        if(agregar_comprar=="Btn_comprar_ahora"):
            print("Btn_comprar_ahora")
            a=comprobar_stock(arreglo,1)
            return redirect("/crear_pedidos/")
        else:
            print("Btn_agregar_carrito")
            a=comprobar_stock(arreglo,1)
            if(not a):
                mensaje="No hay stock suficiente"

    return render(request,"arreglo_detalle.html", {
        "arreglo":arreglo_detail,
        "Arreglos":Arreglos,
        "mensaje":mensaje,
        "categorias":categorias,
    })
    


def carrito(request):
    total=calcularTotales()
    mensaje=""
    mensaje2=""
    if(request.method=="POST"):
        opcion= request.POST.get("opcion")
        if(opcion=="proceder_pago"):
            return redirect("/crear_pedidos/")
        id=request.POST["id"]
        arreglo=Arreglo.objects.get(id=id)
       
        if(opcion=="mas"):
            respuesta=comprobar_stock(arreglo,1)
            if(not respuesta):
                mensaje="No hay suficiente stock"
        elif(opcion=="menos"):
            comprobar_stock(arreglo,-1)
            pass
        elif(opcion=="eliminar"):
            eleminarCarrito(arreglo)
        
        total=calcularTotales()


    cantidad_y_arreglo=list(zip(arreglosComprar,arreglosCantidades,totalValorArreglo))
    if(len(arreglosComprar)==0):
        mensaje2="Tu carrito de compras esta vacio"
    print(cantidad_y_arreglo)
    return render(request, "carrito.html",{
        "cantidad_y_arreglo":cantidad_y_arreglo,
        "total":total,
        "mensaje":mensaje,
        "categorias":categorias,
        "mensaje2":mensaje2
    })



def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@ejemplo.com', '15218418')
        return HttpResponse("✅ Usuario admin creado!")
    return HttpResponse("⚠️ El usuario admin ya existe")