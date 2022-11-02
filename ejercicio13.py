# Escribir un programa que muestre el eco de t0d0 lo que el usuario introduzca
#  hasta que el usuario escriba “salir” que terminará.

usuario = input("")

while usuario != "salir":
    print(usuario)
    usuario = input("")
print("Has salido del bucle :D")
