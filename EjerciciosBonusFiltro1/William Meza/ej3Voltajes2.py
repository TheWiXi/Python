sum=0
for i in range(3):
    voltaje=float(input(f"Ingrese el valor del voltaje {i+1}: "))
    sum+=voltaje
promedio=sum/3
print(f"{promedio} V. ")
if promedio<115 :
    print("VOLTAJE CORRECTO. ")
elif promedio>115 and promedio<220 :
    print("ALTO VOLTAJE ! ")
else :
    print("PELIGRO !!")