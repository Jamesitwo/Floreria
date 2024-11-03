arreglosComprar=[]
arreglosCantidades=[]
totalValorArreglo=[]


def comprobar_stock(arreglo,accion):
    print("entro a comprobar stock")
    stock=arreglo.stock
    try:
        index=arreglosComprar.index(arreglo)
        cantidad=arreglosCantidades[index]+accion
        if(cantidad<=stock and cantidad>=1):
            arreglosCantidades[index]=cantidad
            print("entro en try", arreglosCantidades[index])
            return True
        return False
    except:
        arreglosComprar.append(arreglo)
        arreglosCantidades.append(1)
        totalValorArreglo.append(arreglo.precio)
        print("entro en except")
        return True


def calcularTotales():
    total=0

    for i in range(len(arreglosComprar)):
       totalValorArreglo[i]=arreglosCantidades[i]*arreglosComprar[i].precio
       total=total+totalValorArreglo[i]
       #print(arreglosComprar[i].nombre,totalValorArreglo[i])
       pass
    return total


def eleminarCarrito(arreglo):
    index=arreglosComprar.index(arreglo)
    del arreglosComprar[index]
    del arreglosCantidades[index]
    del totalValorArreglo[index]