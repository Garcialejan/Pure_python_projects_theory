class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter # Definimos la misma función pero ahora es un setter
    def name(self, new_name):
        self.__name = new_name
        
        
    @name.deleter 
    def name(self):
        del self.__name
    
    
person1 = Person("Alejandro", 25)

name = person1.name
print(name)

person1.name = "Alberto"

name = person1.name
print(name) # Comprobamos que ahor sí se ha cambiado el nombre sin problema

del person1.nombre