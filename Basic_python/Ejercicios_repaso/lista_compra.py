
titulo = "\nLista de la compra\n"
print(titulo + "-" * len(titulo) + "\n")

lista_compra = []
pregunta = None

while pregunta != "nada":
    pregunta = input("¿Qué desea comprar? (nada, para salir)") #Se pone nada para cerrar el bucle y salir de la lista
    if pregunta == "nada":
        print("Has acabado tu lista de la compra") #Se podría poner un break para romper el while y simplificar el código
    elif pregunta != "nada":
        if pregunta in lista_compra:
            print("Este producto ya está en la lista de tu compra.\n")
        else:
            respuesta = input("Seguro que desea comprar: {} (S/N)".format(pregunta))
            if respuesta == "S":
                lista_compra.append(pregunta)


print("La lista de la compra es: {}".format(lista_compra))
