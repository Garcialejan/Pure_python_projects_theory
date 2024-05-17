
titulo = "Bienvenido al test sobre quesos\n"
print("\n" + titulo + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("¿Sueles comer queso a lo largo de la semana?\n"
            "A- 1 vez por semana\n"
            "B- 3 veces por semana\n"
            "C- Más de 3 veces por semana\n")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Lo siento, las opciones son sólo A, B o C")
    exit()

opcion = input("¿Cómo prefieres la hamburguesa?\n"
            "A- Con queso\n"
            "B- Sin queso\n"
            "C- Con mucho queso\n")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Lo siento, las opciones son sólo A, B o C")
    exit()

opcion = input("¿Cuál de estas es tu pizza favorita?\n"
            "A- Marinara\n"
            "B- Margaritta\n"
            "C- Cuatro quesos\n")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Lo siento, las opciones son sólo A, B o C")
    exit()

print("\n" + "La puntuación obtenida ha sido de: {}".format(puntuacion))

if puntuacion >= 40:
    print("\n" + "Eres un verdadero amante de los quesos!!")
elif puntuacion >= 30:
    print("\n" + "Definitivamente te gusta el queso")
else:
    print("\n" + "Siento decirte que no eres un fan de los quesos")