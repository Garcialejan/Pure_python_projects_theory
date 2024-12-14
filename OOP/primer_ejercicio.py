class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando...")

nombre = input("Define el nombre del estudiante: ")
edad = input("¿Cuántos años tiene?")
grado = input("¿Qué estudia?")

estudiante_uno = Estudiante(nombre, edad, grado)

print(f'''
      Datos del estudiante:\n\n
      Nombre: {estudiante_uno.nombre}\n
      Edad: {estudiante_uno.edad}\n
      Grado: {estudiante_uno.grado}
      ''')

max_intentos = 2
intento = 0
si_estudia = ["yes", "y", "si"]
no_estudia = ["no", "n"]

while intento <= max_intentos:
    estudiar = input("Está estudiando? [y/n]").lower().replace("í", "i")

    if estudiar in si_estudia:
        estudiante_uno.estudiar()
        break
    elif estudiar in no_estudia:
        print(f"{estudiante_uno.nombre} es un vago y no estudia")
        break
    else:
        intentos_restantes = (max_intentos - intento)
        if intentos_restantes > 1:
            print(f"Te has equivocado, te quedan {intentos_restantes+1} intentos. Escoge entre [y/n]")
        elif intentos_restantes == 1:
            print(f"Te has equivocado, te queda {intentos_restantes+1} intentos. Escoge entre [y/n]")
        else:
            print("Espabila crack, escoge algo que sea correcto a la próxima")
    
    intento += 1

