# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo que tenga
# tantas líneas como el número introducido, como el triángulo de más abajo.

numero = int(input("Introduce un número: "))

for i in range(1, numero+1):
    for x in range(2*i-1, 0, -2):
        print(x, end="")
    print("")
