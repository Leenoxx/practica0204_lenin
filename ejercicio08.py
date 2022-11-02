# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1, 11):
    x = 1
    while x <= 10:
        print(i * x, end = " ")
        x += 1
    print("")
