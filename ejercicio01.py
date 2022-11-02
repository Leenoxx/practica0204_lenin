# Escribir un programa que almacene la cadena de caracteres
# contraseña en una variable, pregunte al usuario por la contraseña
# e imprima por pantalla si la contraseña introducida por el
# usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = "contraseña"
contraseña_2 = input("Escribe la contraseña: ")

if contraseña == contraseña_2.lower():
    print("La contraseña es CORRECTA.")
else:
    print("La contraseña es INCORRECTA")
