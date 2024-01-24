sum=0
for i in range(5):
    voltaje=float(input(f"Ingrese el valor del voltaje {i+1}: "))
    sum+=voltaje
promedio=sum/5
print(f"{promedio} V. ")
if promedio>220 :
    print("ALTO VOLTAJE ! ")
else :
    print("VOLTAJE CORRECTO. ")
