from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="index"),#es mejor usar nombres en las urls, por si en un futuro se requiere cambiar alguna 
    path("contacto/",views.contacto),  
    path("arreglos/",views.Arreglos),

    path("crear_pedidos/<int:id>",views.crear_pedido),

    path("arreglo/<int:id>",views.arreglo_detalle),
    path("carrito/",views.carrito)
]