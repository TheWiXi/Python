temperatura=float(input("Ingrese la temperatura: "))
presion=float(input("Ingrese la presion: "))
if (presion>200):
    print("ALARMA.")
else:
    if (temperatura>100):
      print("ALARMA.")
    else:
     print("NORMAL.")

