import random

num_adivinar = random.randint(1,10)
num_prueba = int(input("¿En qué número del 1 al 10 estoy pensando? "))

if num_prueba == num_adivinar:
    print("Has acertado, !ENHORABUENA!")

print("El número ganador era: {}".format(num_adivinar))








