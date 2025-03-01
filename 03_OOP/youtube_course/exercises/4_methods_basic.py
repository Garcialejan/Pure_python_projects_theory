class Character:
    def __init__(self, name, stregth, speed):
        self.name = name
        self.stregth = stregth
        self.speed = speed
        
    def __repr__(self):
        return f"{self.name} (Stregth: {self.stregth}, Speed: {self.speed})"
    
    def __add__(self, other_ch):
        new_name = self.name + "-" + other_ch.name
        new_stregth = round(((self.stregth + other_ch.stregth)/2)**1.2)
        new_speed = round(((self.speed + other_ch.speed)/2)**1.2)
        return Character(new_name, new_stregth, new_speed)
    
goku = Character("Goku", 100, 100)
vegeta = Character("Veggeta", 90, 95)

gogeta = goku + vegeta
print(gogeta)