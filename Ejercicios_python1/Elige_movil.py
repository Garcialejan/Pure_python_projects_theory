
titulo = "Bienvenido a tu selector de móviles"
print("\n" + titulo + "\n" + len(titulo) * "_" + "\n")

opcion1 = "iphone ultra pro max"
opcion2 = "iphone de segunda mano"
opcion3 = "android chino de 100 euros"
opcion4 = "google pixel supercamara"
opcion5 = "android calidad-precio"

tipo_de_movil = input("¿Qué tipo de movil quieres comprar? \n"
                      "A- Android \n"
                      "B- IOs \n")

if tipo_de_movil == "A": #Ha contestado Android
    dinero = input("¿Tiénes dinero? \n"
                   "A- No \n"
                   "B- Si \n")
    if dinero == "A":
        print("El móvil que debes comprarte es: {}".format(opcion3))
    else:
        camara = input("¿Quieres una buena cámara para tu teléfono? \n"
                       "A- No \n"
                       "B- Si \n")
        if camara == "A":
            print("El móvil que debes comprarte es: {}".format(opcion5))
        else:
            print("El móvil que debes comprarte es: {}".format(opcion4))

elif tipo_de_movil == "B": #Ha contestado IOs
    dinero = input("¿Tiénes dinero? \n"
                   "A- No \n"
                   "B- Si \n")
    if dinero == "A":
        print("El móvil que debes comprarte es: {}".format(opcion2))
    else:
        print("El móvil que debes comprarte es: {}".format(opcion1))

else:
    print("\n" + "Lo siento, tienes que elegir entre android (opción A) o IOs (opcion B)")

