
edad = int(input("¿Qué edad tienes? "))
tipo_de_carnet = input("Si tienes un carnet, dime de que tipo es: (E para estudiante / F para familia numerosa "
                       "/ P para pensionista / N para nada) ")

if (((25 <= edad <= 35) and tipo_de_carnet == "E") or edad <= 10
        or (edad >= 65 and tipo_de_carnet == "P") or tipo_de_carnet == "F") :

    print("Se te aplica el descuento del 25%")

else:
    print("No se te aplica el descuento")

