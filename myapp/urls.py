from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="index"),#es mejor usar nombres en las urls, por si en un futuro se requiere cambiar alguna 
    path("contacto/",views.contacto),  
    path("arreglos/<str:categoria>",views.Arreglos),

    path("crear_pedidos/",views.crear_pedido),

    path("arreglo_detalle/<int:id>",views.arreglo_detalle),
    path("carrito/",views.carrito),
    path('createadmin/', views.create_admin),
]



