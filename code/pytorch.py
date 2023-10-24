class game:
    def __init__(self, name, health, power, speed, armor):
        self.name = name
        self.health = health
        self.power = power
        self.speed = speed
        self.armor = armor

    def attack(self, hero):
        hero.health -= self.power
        return hero.health
    


a = game('blacksmith', 1000, 500, 95, 800)
b = game('yuri gagarin', 965, 750, 100, 65)

a.attack(b)
print(f"{a.name} telah menyerang {b.name} healthnya jadi {b.health}")
    