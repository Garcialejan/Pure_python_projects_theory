
import random

gameover = "GAME OVER"
titulo = "Bienvenido a esta aventura en la que tendrás que escapar para ganar"
print("\n" + titulo + "\n" + len(titulo) * "_" + "\n"
      "En este nuevo juego de tu creador favorito, Elbicho, un malvado \n"
      "hombre te persigue con el objetivo de secuestrate por lo que debes\n"
      "huir. \n"
      "\n"
      "Estás atrapado en una habitación de la casa y tienes dos opciones: \n"
      "una puerta semiabierta o una rendija de ventilación en el techo. \n")

opcion = input("¿Que opción de escape eliges inicialmente?\n"
               "A) Puerta semiabierta\n"
               "B) Rendija de ventilación\n")

if opcion == "A":
    print ("Entras en un pasillo en el que el malvado hombre te empieza a perseguir.\n"
           "Tienes dos opciones, correr por el pasillo en el que no ves el final o \n"
           "forzar una puerta que encuentras por el pasillo.\n")
    opcion = input ("¿Qué opción eliges?\n"
                    "A) Correr por el pasillo\n"
                    "B) Forzar una de las puertas\n")
    if opcion == "A":
        print("Llegas al final del pasillo en el que hay unas escaleras, como no ves,\n"
              "porque está muy oscuro, no ves las escaleras que hay y te caes hasta\n"
              "abajo, rompiendote un tobillo.\n"
              "\n",
              gameover + "\n" + len(gameover) * "_")
    elif opcion == "B":
        print("Atrancas la puerta para que no pueda entrar. En esta nueva habitación\n"
              "ves una ventana que lleva al exterior pero que está bloqueada con un \n"
              "candado y la combinación es una operación matemática. También hay otra \n"
              "puerta, pero no sabes hacia donde lleva.\n")
        opcion = input("¿Qué opción eliges?\n"
                       "A) Intentas desbloquear el candado y escapar por la ventana\n"
                       "B) Ni de coña, soy muy malo en mates, elijo probar suerte con la puerta\n")
        if opcion == "A":
            combinacion_candado = random.randint(1,5) * 2
            print ("Solo puedes probar un número par entre el 2 y el 10. Si no aciertas \n"
                   "el candado se bloquea. ¡RÁPIDO, EL HOMBRE ESTÁ FORZANDO LA PUERTA QUE \n"
                   "HAS ATRANCADO ANTES!\n")
            prueba_candado = int(input("El número que pruebas es el: \n"))
            if prueba_candado == combinacion_candado:
                print ("¡Has acertado! Abres la ventana y escapas al exterior, en el que \n"
                       "hay un formula 1 conducido por en Nano que te llevará a casa, pero \n"
                       "primero hará una paradita en el circuito para demostarte porque la 33\n"
                       "está más cerca que nunca")
            else:
                print("Has fallado y el candado ha quedado bloqueado, el hombre entrá en la habitación\n"
                      "y te secuestra.\n ",
                      gameover + "\n" + len(gameover) * "_")
        elif opcion == "B":
            print ("La puerta está atrancada y no puedes abrirla. Encuentras un cuchillo \n"
                   "y decides enfrentarte al hombre, sin embargo este es un maestro con los \n"
                   "cuchillos ya que es un chef de renombre, por lo que además de secuestrarte \n"
                   "te hiere de gravedad y te da la turra contandote como elaborar la\n"
                   "                 VERDADERA PAELLA VALENCIANA \n",
                    gameover + "\n" + len(gameover) * "_")
        else:
            print("Las opciones son A o B. Si no quieres descubrir la historia deberías cerrar el juego")
    else:
        print("Las opciones son A o B. Si no quieres descubrir la historia deberías cerrar el juego")

elif opcion == "B":
    opcion = input("Abres la rendija de la habitación y escapas a través de ella. A través de las rendijas\n"
                   "observas como el hombre te busca por un pasillo muy oscuro. En el conducto de ventilación\n"
                   "observas un ventilador parado. Una de sus aspas podría servirte como arma para protegerte.\n"
                   "¿Lo coges? o ¿prefieres no jugartela y no hacer ruido?\n"
                   "A) Coges el aspa\n"
                   "B) No la coges\n")
    if opcion == "A":
        aspa_inventario = True
    elif opcion == "B":
        aspa_inventario = False

    print("Tras recorrer el conducto de ventilación llegas a una habitación en la que ves que hay una ventana\n"
          "que lleva al exterior. Decides bajar en esa habitación, pero te das cuenta que la venatana está\n"
          "bloqueada con un candado y la combinación es una operación matemática.\n")
    combinacion_candado = random.randint(1, 5) * 2

    print("Solo puedes probar un número par entre el 2 y el 10. Si no aciertas el candado se bloquea. ¡RÁPIDO,\n"
          "EL HOMBRE ESTÁ POR EL PASILLO Y PUEDE INTENTAR ABRIR LA PUERTA!")
    prueba_candado = int(input("El número que pruebas es el: \n"))

    if prueba_candado == combinacion_candado:
        print("¡Has acertado! Abres la ventana y escapas al exterior, en el que \n"
              "hay un formula 1 conducido por en Nano que te llevará a casa, pero \n"
              "primero hará una paradita en el circuito para demostarte porque la 33\n"
              "está más cerca que nunca")
    else:
        print("Has fallado y el candado ha quedado bloqueado, el hombre entrá en la habitación.\n")
        if aspa_inventario == True:
            print ("Como sí has cogido el aspa, tienes una lucha a muerte en la que consigues herir\n"
                   "de gravedad al hombre que intentaba secuestrarte. PUEDES ESCAPAR SIN PROBLEMAS\n")
        elif aspa_inventario == False:
            print("Has fallado y el candado ha quedado bloqueado, el hombre entrá en la habitación\n"
                  "Como no has cogido el aspa, no puedes defenderte y el hombre te secuestra.\n",
                  gameover + "\n" + len(gameover) * "_")
else:
    print("Las opciones son A o B. Si no quieres descubrir la historia deberías cerrar el juego")

