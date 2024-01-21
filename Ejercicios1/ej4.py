base=float(input("Ingrese el valor de la base: "))
altura=float(input("Ingrese el valor de la altura: "))
if (base>0):
    if (altura>0):
        print(f"El area del rectangulo es: {base*altura}")
    else:
        print("La altura debe ser positiva.")
else:
    print("La base debe ser positiva.")    