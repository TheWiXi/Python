consumo=int(input("Ingrese el valor de su consumo: "))
if (consumo>130000):
    print(f"El total a pagar es: {consumo*0.85}")
else:
    print(f"El total a pagar es: {consumo}")
