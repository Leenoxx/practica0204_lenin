# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo como el de
# más abajo, de altura el número introducido.

numero = int(input("Introduce un número: "))

for i in range(1, numero+1):
    for x in range(i):
        print("*", end="")
    print("")
