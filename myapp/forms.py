from django import forms

class crearPedido(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=30)
    email=forms.EmailField()
    cedula=forms.CharField(label="Cedula", max_length=15)
    celular=forms.CharField(label="Telefono", max_length=10)
    nombreR=forms.CharField(label="Nombre de quien recibe", max_length=30)
    direccion=forms.CharField(label="Direccion", max_length=30)
    muicipio=forms.CharField(label="Minicipio", max_length=20)
    barrio=forms.CharField(label="Barrio", max_length=30)
    celularR=forms.CharField(label="Celular de quien recibe", max_length=10)
    quienEnvia=forms.CharField(label="Quien envia", max_length=30)
    #fechaenvio=forms.DateTimeField(label="Fecha Envio")
    mensaje=forms.CharField(label="Mensaje",widget=forms.Textarea)
    #id_arreglo= forms.IntegerField()


