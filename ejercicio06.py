# Escribir un programa que pregunte al usuario su edad y
# muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Introduce tú edad: "))
contador = 1

while contador <= edad:
    print(contador)
    contador = contador + 1
