usuarioc="ADMINISTRADOR"
contraseñac="Admin123"
usuario=input("Usuario: ").upper()
contraseña=input("Contraseña: ")
if (usuario==usuarioc):
    if(contraseña==contraseñac):
        print("BIENVENID@!")
    else:
        print("ERROR")
else:
    print("ERROR")