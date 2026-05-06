class GameCharacter: 

    def __init__(self, name, health): 
        self.name = name 
        self.health = health 

    def attack(self): 
        print(f"{self.name} attacks!")

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        damage = min(amount, self.health)
        print(f"{self.name} took {damage} points of damage. Remaining Health: {self.health}")
    
    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} is alive!")
        else:
            print(f"{self.name} is dead:(")
        return

Steve = GameCharacter("Steve", 100)

Steve.attack()
Steve.take_damage(50)
Steve.is_alive()
Steve.take_damage(60)
Steve.is_alive()