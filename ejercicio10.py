# Escribir un programa que almacene la cadena de caracteres contraseña
# en una variable, pregunte al usuario por la contraseña hasta que
# introduzca la contraseña correcta.

contraseña_uno = input("Escribe una contraseña para almacenarla: ")
contraseña_dos = input("Vuelve a escribir la contraseña para acceder: ")

while contraseña_dos != contraseña_uno:
    print("CONTRASEÑA INCORRECTA")
    contraseña_dos = input("Vuelve a escribir la contraseña para acceder: ")

print("CONTRASEÑA VÁLIDA")
