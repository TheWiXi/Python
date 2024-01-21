anual=14400000
mensual=(anual/12)
tiempo=float(input("Ingrese el tiempo que lleva en la empresa: "))
if (tiempo>=10):
    print(f"Su aumento mensual sera: {mensual*1.1} y Anual de: {anual*1.1}")
elif (tiempo<10) and (tiempo>5):
    print(f"Su aumento mensual sera: {mensual*1.07} y Anual de: {anual*1.07}")
elif(tiempo<5)and(tiempo>3):
    print(f"Su aumento mensual sera: {mensual*1.05} y Anual de: {anual*1.05}")
else:
    print(f"Su aumento mensual sera: {mensual*1.03} y Anual de: {anual*1.03}")

