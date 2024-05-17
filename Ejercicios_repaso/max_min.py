"""
#Busca el máx y el min de una lista de números

lista_usuario = []

#Definimos los números que quiere introducir el usuario

numero_introducido = int(input("Introduce un número en la lista: "))
lista_usuario.append(numero_introducido)

while input("Desea introducir un número nuevo en la lista: [SI/NO]") == "SI":
    numero_introducido = int(input("Introduce un número en la lista: "))
    lista_usuario.append(numero_introducido)

print(lista_usuario)
"""

#Introducimos una forma más sencilla y óptima de introducir los números

numeros_introducidos = input("Introduzca los números separados por una coma: ") #1,2,3,4,5,6,7,8,9
lista_numeros = numeros_introducidos.split(",")
numeros_limpios = []

for numero in lista_numeros:
    numeros_limpios.append(int(numero))

print(numeros_limpios)

print("El número más grande es: {}".format(max(numeros_limpios)))
print("El número más pequeño es: {}".format(min(numeros_limpios)))


"""
#List comprehesion. Optimizamos el código anterior

numeros_introducidos = input("Introduzca los números separados por una coma: ") #1,2,3,4,5,6,7,8,9
lista_numeros = numeros_introducidos.split(",")

lista_numeros = [int(numeros) for numero in lista_numeros]

print(lista_numeros)
print("El número más grande es: {}".format(max(lista_numeros)))
print("El número más pequeño es: {}".format(min(lista_numeros)))
"""

