class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")

class Artista:
    def __init__(self, habilidad: str):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return self.habilidad
        

class EmpleadoArtista(Persona, Artista): # Subclase que hereda métodos y atributos de Persona y Artista
    def __init__(self, nombre: str, edad: int, nacionalidad: str, habilidad: str,  salario: int, empresa: str):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return (f'Hola soy {self.nombre}, mi habilidad es {super().mostrar_habilidad()} y trabajo en {self.empresa}')
    

alejandro = EmpleadoArtista("Alejandro", 32, "Español", "beber", 30000, "CPS")

herencia_1 = issubclass(EmpleadoArtista, Persona)
herencia_2 = issubclass(Artista, Persona)
instancia_1 = isinstance(alejandro, EmpleadoArtista)
instancia_2 = isinstance(alejandro, Persona)
instancia_3 = isinstance(alejandro, Artista)

print(herencia_1, herencia_2, instancia_1, instancia_2, instancia_3)


carlos = Artista("Cantar")
herencia_carlos_1 = isinstance(carlos, Persona)
herencia_carlos_2 = isinstance(carlos, EmpleadoArtista)
herencia_carlos_3 = isinstance(carlos, Artista)

print(herencia_carlos_1, herencia_carlos_2, herencia_carlos_3)