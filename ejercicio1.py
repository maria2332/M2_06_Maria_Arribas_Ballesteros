import math

def area_circulo():
 radio = input("Introduce el valor del radio: ")
 radio=int(radio)
 area = math.pi * (radio**2)
 return print(area)

area_circulo()