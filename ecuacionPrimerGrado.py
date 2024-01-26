print("A continucacion ingrese los coeficientes de la ecuacion ax + b= 0")
a=float(input("Ingrese el coeficiente a: "))
b=float(input("Ingrese el coeficiente b: "))
#x=-b/a
if a == 0 :
    print(f"La ecuacion {a}x + {b}=0 NO TIENE SOLUCION. ")
elif (a==0) and (b==0) :
    print(f"Para la ecuacion {a}x + {b}=0 NO HAY SOLUCION UNICA. ")
else :
    x = (-b)/a
    print(f"Para la ecuacion {a}x + {b}=0 SOLUCION UNICA: x={x}")
