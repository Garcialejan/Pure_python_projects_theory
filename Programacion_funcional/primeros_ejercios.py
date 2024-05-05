import random


def potencia_primera_opcion(base, *args):
    if args:
        potencia = (base ** args[0]) # Los corchetes para usa el primer elemento de la tupla como exponente.
        # Podría generar problemas si hay más de un elemento en la tupla. No es la mejor forma de hacerlo.
    else:
        potencia = (base ** 2)

    return potencia

def potencia_segunda_opcion(base, exponente = 2):
    resultado = base
    for a in range(1, exponente):
        resultado *= base
    return resultado

def fibonaci_recursivo(n):
    if n <= 1:
        return 1
    return fibonaci_recursivo(n-1) + fibonaci_recursivo(n-2)

def fibonacci_no_recursivo(n):
    fib_sequence = [1, 1] #Debe tener al menos los dos primeros elementos de la serie antes de entrar al bucle,
                          #evitando así el error de "list index out of range"
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

def largo_string(string1, *args): #He tenido que buscar ayuda con chatGPT
    # Primero, se define la longitud de las cadenas
    largos = [len(string1)]
    for a in args:
        largos.append(len(a))
    # Encuentra la cadena más larga
    cadena_mas_larga = max([string1] + list(args), key=len)
    numero_max_string = max(largos)

    resultado = "La string más larga es {} y está formada por {} letras".format(cadena_mas_larga, numero_max_string)
    return resultado

def suma(*numeros):
    resultado = 0
    for n in numeros:    #Iterate over all arguments passed to the function
        resultado += n    #We accumulate the value of each number in the result variable
    return resultado

def es_impar(numero):
    comprobacion = numero % 2
    if comprobacion != 0:
        par_o_impar = True
    else:
        par_o_impar = False
    return par_o_impar

def si_o_no():
    respuesta = input("¿Estás seguro?¿si o no?")
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Esa contestación no es válida. Contesta [si] o [no]")
    if respuesta == "si":
        resultado = True
    elif respuesta == "no":
        resultado = False
    return resultado

def conversor_mayusculas(): #He tenido que buscar ayuda con chatGPT
    texto = input("Ingresa una texto: ")
    texto_mayus = "" #Inicializa una string vacía para almacenar el texto en mayúsculas
    for letra in texto: #Itera sobre cada letra en el texto ingresado
        if 'a' <= letra <= 'z': # Verifica si la letra está en minúscula
            letra = chr(ord(letra) - ord('a') + ord('A')) # Convierte la letra a mayúscula sumándole la diferencia entre 'a' y 'A'
        texto_mayus += letra # Agrega la letra (ya sea en mayúscula o no) a la cadena de texto en mayúsculas
    print("Palabra en mayúsculas: {}".format(texto_mayus))
    return texto_mayus

def adivina_numero():
    numero_elegido = int(input("Elige un número del 1 al 100"))
    numero_adivinar = random.randint(1, 100)
    lista_numeros_elegidos =[]
    while numero_elegido != numero_adivinar:
        numero_elegido = int(input("Has fallado. Elige otro número del 1 al 100"))
        lista_numeros_elegidos.append(numero_elegido)
    if numero_elegido == numero_adivinar:
        print("Enhorabuena el número {} es el correcto".format(numero_adivinar))
    return numero_elegido


def main():
    print(adivina_numero())

if __name__ == "__main__":
    main()
