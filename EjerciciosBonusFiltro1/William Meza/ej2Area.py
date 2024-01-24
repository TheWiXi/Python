lado1=float(input("Ingrese el valor del lado 1 del triangulo: "))
lado2=float(input("Ingrese el valor del lado 2 del triangulo: "))
lado3=float(input("Ingrese el valor del lado 3 del triangulo: "))
area=0
if lado1 == lado2 == lado3 :
    area=(lado1*lado2)/2
    if area>1000:
        print("DATOS NO VALIDOS. ")
    else :
        print(f"El area del triangulo es: {area}")
else:
    print("El triangulo no es equilatero.")