
SALIDA = "salir"

productos_disponibles = ["Pan", "pollo", "leche", "chocolate", "harina", "huevos"]

def pregunta_producto_usuario():
    producto_elegido = input("Introduce un producto en la lista [{} para salir]".format(SALIDA))
    while producto_elegido.lower() not in productos_disponibles and producto_elegido != SALIDA: #.lower para asegurar que este en minúsculas
        print("El producto seleccionado no está en la lista de los productos disponibles")
        producto_elegido = input("Introduce un producto en la lista [{} para salir]".format(SALIDA))
    return producto_elegido


def guardar_lista_archivo(lista_compra): #Definimos una función que genere un archivo de texto en el que se guarde nuestra lista de la compra
    nombre_fichero = input("¿Cómo quieres que se llame tu lista/archivo?")
    with open(nombre_fichero + "txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))



def main():
    lista_compra = []
    input_usuario = pregunta_producto_usuario()

    while input_usuario != SALIDA:
        lista_compra.append(input_usuario)
        print("\n".join(lista_compra))
        input_usuario = pregunta_producto_usuario()

    guardar_lista_archivo(lista_compra)



if __name__ == "__main__":
    main()
