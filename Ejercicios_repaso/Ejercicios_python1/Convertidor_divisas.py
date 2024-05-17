
titulo = "Bienvenido a tu convertidor de divisas favorito"
print("\n" + titulo + "\n" + len(titulo) * "_" + "\n")

dolar_to_euro = float(input("¿A cuánto está el cambio de dolar a euro? \n"))
libra_to_euro = float(input("¿A cuánto está el cambio de libra a euro? \n"))

opcion = input("¿Qué tipo e moneda quieres cambiar?¿Dolares (D), euros (E) o libras (L)? \n")

if opcion == "E" or opcion == "euros":
    cantidad_inicial = float(input("¿Cuántos euros tienes \n"))
    tipo_de_cambio = input("¿Quieres cambiar a dolares (D) o a libras (L) \n")

    if tipo_de_cambio == "D":
        cantidad_final = cantidad_inicial / dolar_to_euro
        print("\n" + "Tú cmabio se ha realizado con exito, tienes {} euros".format(cantidad_final))
    else:
        cantidad_final = cantidad_inicial / libra_to_euro
        print("\n" + "Tú cmabio se ha realizado con exito, tienes {} libras".format(cantidad_final))

elif opcion == "D" or opcion == "dolares":
    cantidad_inicial = float(input("¿Cuántos dolares tienes \n"))
    tipo_de_cambio = input("¿Quieres cambiar a euros (E) o a libras (L) \n")

    if tipo_de_cambio == "E":
        cantidad_final = cantidad_inicial * dolar_to_euro
        print("\n" + "Tú cmabio se ha realizado con exito, tienes {} dolares".format(cantidad_final))
    else:
        cantidad_final = cantidad_inicial * dolar_to_euro / libra_to_euro
        print("\n" + "Tú cmabio se ha realizado con exito, tienes {} libras".format(cantidad_final))

elif opcion == "L" or opcion == "libras":
    cantidad_inicial = float(input("¿Cuántas libras tienes \n"))
    tipo_de_cambio = input("¿Quieres cambiar a euros (E) o a dolares (D) \n")

    if tipo_de_cambio == "E":
        cantidad_final = cantidad_inicial * libra_to_euro
        print("\n" + "Tú cmabio se ha realizado con exito, tienes {} euros".format(cantidad_final))
    else:
        cantidad_final = cantidad_inicial * libra_to_euro / dolar_to_euro
        print("\n" + "Tú cmabio se ha realizado con exito, tienes {} dolares".format(cantidad_final))
else:
    print("Lo siento, solo podemos realizar cambio de divisas entre euros (E), dolares (D) y libras (L). "
          "(Recuerda las mayúsculas!!)")