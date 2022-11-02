# Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin,
# de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres
# con un nombre anterior a la M y los hombres con un nombre posterior a la
# N y Slytheryn por el resto. Escribir un programa que pregunte al usuario
# su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sexo = input("Introduce tu sexo (H/M): ")
nombre = input("Escribe tu nombre: ")

if sexo == "H":
    if nombre[0] <= "M":
        print("Perteneces a Slytheryn")
    elif nombre[0] >= "N":
        print("Perteneces a Gryffindor")


elif sexo == "M":
    if nombre[0] <= "M":
        print("Perteneces a Gryffindor")
    elif nombre[0] >= "N":
        print("Perteneces a Slytheryn")
