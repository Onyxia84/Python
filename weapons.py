from caracters import hero

Link = hero("Bob", 1, 0)
Link.attack

class weapons():
    def __init__(self, name, damage, miss_rate) :
        self.name = name
        self.damage = damage
        self.miss_rate = miss_rate
    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Miss Rate: {self.miss_rate}%)"

Blade = weapons("Blade of the lich king", 80, 10)
Bow = weapons("Sylvanas Bow", 100, 20)
Knife = weapons("Knife", 50, 10)

all_weapons = [Knife]