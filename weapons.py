# Import the hero class from the caracters module
from caracters import hero

# Base class for weapons in the game
class Weapons:
    def __init__(self, name, damage, miss_rate):
        self.name = name  # Name of the weapon
        self.damage = damage  # Damage dealt by the weapon
        self.miss_rate = miss_rate  # Percentage chance of missing an attack
    
    # String representation of the weapon
    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Miss Rate: {self.miss_rate}%)"

# Create instances of various weapons with specific attributes
Blade = Weapons("Blade of the Lich King", 155, 30)
Bow = Weapons("Sylvanas Bow", 140, 20)
Knife = Weapons("Knife", 80, 10)
Lucky = Weapons("Lucky", 400, 85)
Safy = Weapons("Safy", 100, 0)

# List containing all weapon instances for easy reference
all_weapons = [Knife, Blade, Bow, Lucky]
