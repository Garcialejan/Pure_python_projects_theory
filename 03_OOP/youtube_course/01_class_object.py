class Mobile:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas realizando una llamada desde un: {self.modelo}")
    
    def colgar(self):
        print(f"Acabas de colgar la llamada desde el: {self.modelo}")

movil_uno = Mobile("Samsung", "S23", "48MP")
movil_dos = Mobile("Iphone", "15 pro", "96MP")


movil_uno.llamar()
movil_uno.colgar()