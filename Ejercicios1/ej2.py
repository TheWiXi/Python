figura=input("Ingrese T si desea el area de un triangulo o C si desea el area de un circulo: ").upper()
if (figura=="T"):
    base=float(input("ingrese el valor de la base(cm): "))
    altura=float(input("ingrese el valor de la altura(cm): "))
    print(f"El valor del area es: {base * altura * 0.5}")
elif (figura=="C"):
    radio=float(input("ingrese el valor del radio: "))
    print(f"El valor del area es: {3.14*(radio**2)}")
else:
    print("La letra ingresada no es una de las indicadas.")