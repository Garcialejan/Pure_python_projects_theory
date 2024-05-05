
#Primero preguntamos de que número quiere obtener su tabal de multiplicar

numero = int(input("¿Qué número quieres multiplicar?\n"))
lista_numero = range(1, 11)

for n in lista_numero:
    print ("{} X {} = {}".format(numero, n, n * numero))