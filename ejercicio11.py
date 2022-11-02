# Escribir un programa que pida al usuario una palabra y luego muestre
# por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Escribe una palabra: ")

longitud = len(palabra)

for i in range(longitud-1, -1, -1):
    print(palabra[i])
