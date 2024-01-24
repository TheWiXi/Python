start=True
op=0
while start :
    metros=float(input("Ingrese su distancia en metros(m): "))
    print(f"Su distancia en kilometros es: {metros/1000} Km")
    op=input("Si desea convertir otra distancia ingrese la letra S de lo contrario ingrese la letra N: ").upper()
    if op == "S":
        pass
    elif op == "N":
        start=False
    
