n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo numero: "))
n3 = int(input("Introduce el tercer numero: "))
print("El número más grande entre {}, {} y {} es {} y el número más pequeño es {}"
      .format(n1, n2, n3, max(n1,n2,n3), min(n1,n2,n3)))

