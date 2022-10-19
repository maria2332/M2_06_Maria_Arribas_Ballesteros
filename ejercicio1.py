import math

def area_circulo():
 radio = int(input("Introduce el valor del radio: "))
 area = math.pi * (radio^2)
 return area 

print(area_circulo())