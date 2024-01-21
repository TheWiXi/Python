import os 

menu = """
    ++++++++++++++++++++++++++++++++
    +++++     BIENVENIDO!      +++++
    ++++++++++++++++++++++++++++++++

    Opciones:
    1.Registrar un equipo.
    2.Registrar una fecha.
    3.Ver tabla de posiciones.
    4.Salir.
"""
start = True #variable de inicio
equipos = [                             #lista de equipos(tabla de posiciones)
    # ['BUCAROS', 4, 3, 0, 1, 5, 3, 0],
    # ['CALI', 4, 2, 1, 1, 1, 3, 0],
    # ['JUNIOR', 4, 1, 2, 1, 2, 4, 0],
    # ['AMERICA', 4, 2, 1, 1, 1, 3, 0],
    # ['ALIANZA', 0, 2, 1, 1, 3, 2, 0]
]
fechas = [] #lista de fechas (tabla de enfrentamientos)
maxgoles=0 #goles del goleador
goleador="" #equipo con mas goles
maxpuntos=0 #puntos ganador
winner="" #ganador
ganados=0 #partidos ganados
ganador="" #equipo con mas puntos (ganador)
golest=0 #total de goles en el campeonato
partidost=0 #total de enfrentamientos

pos = 0
while start == True:
    os.system('cls')
    print(menu)
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        new = input("Ingrese el nombre del equipo: ").upper().replace(" ", "")
        if not any(new == equipo[0] for equipo in equipos):
            equipos.append([new, 0, 0, 0, 0, 0, 0, 0])
            print(f"El equipo {new} fue creado correctamente. ")
            pos += 1
            os.system('pause')
        else:
            print(f"El {new} ingresado ya fue creado. ")
            os.system('pause')
    elif opcion == 2 :
        fecha=input("Ingrese la fecha a registrar (D/M/AA): ")
        local=input("Ingrese el equipo local: ").upper().replace(" ", "")
        gl=int(input("Ingrese los goles del equipo local: "))
        visitante=input("Ingresa el equipo visitante: ").upper().replace(" ", "")
        gv=int(input("Ingrese los goles del equipo visitante: "))
        fechas.append([fecha,local,gl,visitante,gv])
        golest+=gv+gl
        partidost+=1
        if gl > gv :
            for i, equipo in enumerate(equipos) :
                    if ((equipo[0]) == local):
                        equipo[1] += 1
                        equipo[2] += 1
                        equipo[5] += gl
                        equipo[6] += gv
                    elif((equipo[0] == visitante)):
                        equipo[1] += 1
                        equipo[3] += 1
                        equipo[5] += gv
                        equipo[6] += gl
            os.system('pause')
        elif gv > gl :
            for i, equipo in enumerate(equipos) :
                    if ((equipo[0]) == visitante):
                        equipo[1] += 1
                        equipo[2] += 1
                        equipo[5] += gv
                        equipo[6] += gl
                    elif((equipo[0] == local)):
                        equipo[1] += 1
                        equipo[3] += 1
                        equipo[5] += gl
                        equipo[6] += gv
        else:
             for i, equipo in enumerate(equipos) :
                    if ((equipo[0]) == local):
                        equipo[1] += 1
                        equipo[4] += 1
                        equipo[5] += gl
                        equipo[6] += gv
                    elif((equipo[0] == visitante)):
                        equipo[1] += 1
                        equipo[4] += 1
                        equipo[5] += gv
                        equipo[6] += gl
    elif opcion == 3 :
        for i, equipo in enumerate(equipos) :
            equipo[7]=(equipo[2]*3)+(equipo[4])
            if (equipo[5]>maxgoles) :
                  maxgoles=equipo[5]
                  goleador=equipo[0]
            if equipo[7] > maxpuntos :
                 winner=equipo[0]
                 maxpuntos=equipo[7]         
            if equipo[2]>ganados :
                 ganados=equipo[2]
                 ganador=equipo[0]
    print(f"El equipo con mas goles es {goleador} con un total de {maxgoles} goles. ")
    print(f"El equipo ganador es {winner} con un total de {maxpuntos} puntos. ")
    print(f"El equipo con mas partidos ganados es {ganador} con un total de {ganados} partidos ganados. ")
    print(f"El total de goles del torneo fue: {golest} ")
    print(f"El promedio de goles por partido fue: {golest/partidost} ")
    print("['Equipo', PJ, PG, PP, PE, GF, GC, TP]")
    for i, equipo in enumerate(equipos):
        print(equipo)
    os.system('cls')

