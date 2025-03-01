class Person():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        
    def get_name(self):
        print(f"Name: {self.name}")
    
    
class Student(Person):
    def __init__(self, name:str, age:int, grade:str):
        super().__init__(name, age)
        self.grade = grade
        
    def get_grade(self):
        print(f"Name: {self.grade}")
        
        
estudiante = Student("Alejandro", 25, "Civil Engineering")
estudiante.get_name()
estudiante.get_grade()