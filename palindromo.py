n=int(input("Ingrese un numero para saber si es palindromo: "))
ninv=int(str(n)[::-1])
if n == ninv :
    print(f"El numero {n} ES PALINDROMO. ")
else :
    print(f"El numero {n} NO es palindromo. ")