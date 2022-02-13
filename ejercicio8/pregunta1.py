def impuestos(precio):
    impuesto=float(input("introduzca el porcentaje de impuesto"))
    precio=precio+precio*impuesto/100+precio*0,21
    return print(precio)
impuestos(20)
