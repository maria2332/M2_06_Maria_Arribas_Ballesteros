def imc():
    peso = input("Introduce tu peso: ")
    talla = float(input("Introduce tu altura: "))
    IMC = peso / (talla * talla)
    if IMC < 18.50:
        print("Bajo peso")
    elif IMC >=18.50 25.00) :
        print("Peso normal")
    elif IMC >= 25.00 :
        print("Sobrepeso")
    elif IMC >= 30.00 :
        print("Obesidad")
    return 
