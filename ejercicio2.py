def lee_numero():
    numero = input("Introduce un numero: ")
    return numero

def mayor():
    numero1 = lee_numero()
    numero2 = lee_numero()
    numero3 = lee_numero()

    if numero1 > numero2  and numero1 > numero3 : 
        print("El mayor numero es el", numero1)
    elif numero2 > numero1 and numero2 > numero3 :
        print("El mayor numero es el", numero2)
    else :
        print("El mayor numero es el", numero3)
    return numero1, numero2, numero3

mayor()