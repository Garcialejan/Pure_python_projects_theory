
SALIDA = "salir"
ARCHIVO_LISTA = "lista_compra.txt"

def pregunta_producto_usuario():
    producto_elegido = input("Introduce un producto en la lista [{} para salir]".format(SALIDA))
    return producto_elegido


def guardar_lista_archivo(lista_compra): #Definimos una función que genere un archivo de texto en el que se guarde nuestra lista de la compra
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def guardar_producto_lista(lista_compra, input_usuario):
    if input_usuario.lower() in [a.lower() for a in lista_compra]:  # Transformamos el input y la lista a minúsculas para comprobar si un prodcuto ya está en la lista
        print("Este producto ya está en la lista")
    else:
        lista_compra.append(input_usuario)


def cargar_o_crear_lista():
    lista_compra = []

    if input("¿Quiéres cargar la última lista de la compra? [S/N]") == "S": #Introducimos la opción de cargar una lista anterior
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n") #cada vez que encuentra un enter rompe la string para convertirlo en una lista
        except FileNotFoundError:
            print("Archivo de la compra no encontrado!")

    return lista_compra


def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))

def main():
    lista_compra = cargar_o_crear_lista() #Introducimos la opción de cargar una lista anterior
    mostrar_lista(lista_compra) #Mostramos la lista
    input_usuario = pregunta_producto_usuario() #Preguntamos al usuario que producto quiere añadir

    while input_usuario != SALIDA:
        guardar_producto_lista(lista_compra, input_usuario) #Guardamos el producto que nos dice el usuario en la lista
        input_usuario = pregunta_producto_usuario() #Volvemos a reguntar que producto quiere añadir
    mostrar_lista(lista_compra) #Mostramos la lista
    guardar_lista_archivo(lista_compra) #Guardamos la lista en un archivo


if __name__ == "__main__":
    main()