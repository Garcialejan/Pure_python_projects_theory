import random
import os

vida_inicial_pikachu = 80
vida_inicial_squirttle = 90
vida_pikachu = vida_inicial_pikachu
vida_squirttle = vida_inicial_squirttle
ataque_squirttle = None

while vida_pikachu > 0 and vida_squirttle > 0:
    #Se desenvuelven los turnos de combate

    print("Turno de Pikachu")
    ataque_pikachu = random.randint(1,2)

    if ataque_pikachu == 1:
        print("Pikachu ha elegigo el ataque: Bola voltio")
        vida_squirttle -= 10

        if vida_squirttle <= 0:
            print("\n" + "Tu Squirttle ha sido debilitado. HAS PERDIDO")
            exit()
    elif ataque_pikachu == 2:
        print("Pikachu ha elegigo el ataque: Onda trueno\n")
        vida_squirttle -= 12

        if vida_squirttle <= 0:
            print("\n" + "Tu Squirttle ha sido debilitado. HAS PERDIDO")
            exit()

    resultado_vida_pikachu = 100*(vida_pikachu / vida_inicial_pikachu)
    resultado_vida_squirttle = 100 * (vida_squirttle / vida_inicial_squirttle)
    barra_vida = "#"
    print("La vida del Pikachu es:\n", int(resultado_vida_pikachu) * barra_vida )
    print("La vida del Squirttle es:\n", int(resultado_vida_squirttle) * barra_vida)
    input("Enter para pasar a tu turno...\n")
    os.system("cls") #Para borrar la pantalla. Cuidado, pycharm no lo ejecuta correctamente


    print("Turno de Squirttle")
    ataque_squirttle = input("¿Qué ataque vas a querer realizar?\n"
                            "A- Placaje\n"
                            "B- Pistola de agua\n"
                            "C- Burbuja\n")

    while ataque_squirttle != "A" and ataque_squirttle != "B" and ataque_squirttle != "C":
        ataque_squirttle = input("¿Qué ataque vas a querer realizar?\n"
                                 "A- Placaje\n"
                                 "B- Pistola de agua\n"
                                 "C- Burbuja\n")
    if ataque_squirttle == "A":
        print("Squirttle ha elegigo el ataque: Placaje\n")
        vida_pikachu -= 10
    elif ataque_squirttle == "B":
        print("Squirttle ha elegigo el ataque: Pistola de agua\n")
        vida_pikachu -= 12
    elif ataque_squirttle == "C":
        print("Squirttle ha elegigo el ataque: Burbuja\n")
        vida_pikachu -= 9

    resultado_vida_pikachu = 100 * (vida_pikachu / vida_inicial_pikachu)
    resultado_vida_squirttle = 100 * (vida_squirttle / vida_inicial_squirttle)
    barra_vida = "#"
    print("La vida del Pikachu es:\n", int(resultado_vida_pikachu) * barra_vida)
    print("La vida del Squirttle es:\n", int(resultado_vida_squirttle) * barra_vida)
    input("Enter para pasar a tu turno...\n")
    os.system("cls") #Para borrar la pantalla. Cuidado, pycharm no lo ejecuta correctamente

if vida_pikachu <= 0:
    print("\n" + "El Pikachu ha sido debilitado. ERES EL GANADOR")
