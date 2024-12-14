
#texto de ejemplo introducido por el usuario
texto_usuario = input("Introuzca un texto\n")

#Output esperado. Definimos las variables que queremos que se tengan en cuenta. Objetivo: contabilizar
num_espacios = 0
num_vocales = 0
num_comas = 0
vocales = ["a", "e", "i", "o", "u"]


#Recorremos el texto implementado por el usuario, contabilizando cada uno de los items
for item in texto_usuario:
    if item in vocales:
        num_vocales += 1
    elif item == " ":
        num_espacios += 1
    elif item == ",":
        num_comas += 1

print("El número de vocales es {}, de espacios es {} y de comas es {}.".
      format(num_vocales, num_espacios, num_comas))