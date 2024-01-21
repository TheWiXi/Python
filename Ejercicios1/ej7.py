trabajador=str(input("Ingrese P si el empleado es de planta ó A si el empleado es administrativo: ")).upper()
horas=float(input("Ingrese la cantidad de horas laboradas: "))
if (trabajador=="P") :
    print(f"El valor a pagar es: {horas*20000}")
elif ( trabajador=="A" ):
    print(f"El valor a pagar es: {horas*10000}")
else:
    print("El tipo de trabajador no es correcto.")
