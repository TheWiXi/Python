fila=int(input("Ingrese la fila actual del caballo: "))
columna=int(input("Ingrese la columna actual del caballo: "))
if (1<=fila<=8) and (1<=columna<=8) :
    movimientos = [(-2,1),(-2,-1),(-1,2),(1,2),(2,1),(2,-1),(-1,-2),(1,-2)]
    posibles=[]
    for movimiento in movimientos :
        filapos=fila + movimiento[0]
        columnapos=columna+ movimiento[1]
        if (1<=fila<=8) and (1<=columna<=8) :
            posibles.append((filapos,columnapos))
    for filaM in range(1,9):
        for columnaM in range(1,9):
            if (filaM == fila) and (columnaM == columna):
                print("[🐎]", end=" ")
            elif (filaM,columnaM) in posibles :
                print("[+]", end=" ")
            else:
                print("[ ]", end=" ")
        print()
else:
    print("Debe ingresar coordenadas entre 1 y 8. ")
