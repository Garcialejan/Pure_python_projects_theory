class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")

class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, trabajo: str, salario: int):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, notas: int, universidad: str):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = notas
        self.salario = universidad

roberto = Empleado()

