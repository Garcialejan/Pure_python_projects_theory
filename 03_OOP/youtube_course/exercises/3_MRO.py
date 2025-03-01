class Animal():
    def eat(self):
        print("El animal está comiendo")
    
class Mammal(Animal):
    def breastfeed(self):
        print("El animal está amamantando")
    
    
class Bird(Animal):  
    def fly(self):
        print("El animal está comiendo volando")
    
    
class Bat(Mammal, Bird):
    pass


bat1 = Bat()

print(Bat.mro())