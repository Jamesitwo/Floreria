from django.db import models
from django.utils import timezone


class categorias(models.Model):
    nombre= models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class arreglos(models.Model):
    nombre= models.CharField(max_length=100)
    ImgUrl=models.TextField()
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.TextField()
    diponibilidad=models.BooleanField(default=False)
    categorias=models.ForeignKey(categorias,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

    pass 
class Pedido(models.Model):
    nombre= models.CharField(max_length=30)
    email=models.EmailField()
    cedula=models.CharField(max_length=15)
    celular=models.CharField(max_length=10)
    nombreR=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    muicipio=models.CharField(max_length=20)
    barrio=models.CharField(max_length=30)
    celularR=models.CharField(max_length=10)
    quienEnvia=models.CharField(max_length=30)
    fechaenvio=models.DateTimeField()
    mensaje=models.TextField()
    arreglo=models.ForeignKey(arreglos,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre+" "+str(self.id)

class compras_tienda(models.Model):
    nombre=models.CharField(max_length=20)
    email=models.EmailField()
    cedula=models.CharField(max_length=15)
    celular=models.CharField(max_length=10)
    mensaje=models.TextField()
    arreglo=models.ForeignKey(arreglos,on_delete=models.CASCADE)
    fechaentrega=models.DateTimeField(default=timezone.now)
