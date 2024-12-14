class A:
    def hablar(self):
        print("Hola desde A")

class F(A):
    def hablar(self):
        print("Hola desde F")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
   pass

d = D()

# De la siguiente forma especificamos que el objeto "d" 
# va a ejcutar el método hablar, el cual existe para
# todas las clases, pero ejecutará el de la super clase
# que nosotros le especificamos (en este caso la F)
F.hablar(d) 
B.hablar(d)

print(D.mro())