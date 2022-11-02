# Escribir un programa que pida al usuario dos números y
# muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

dividendo = int(input("Escribe el primer número: "))
divisor = int(input("Escribe el segundo número: "))

if divisor == 0:
    print("ERROR")
else:
    print("El resultado es", dividendo / divisor)
