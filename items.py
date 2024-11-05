class items():
    def __init__(self, name, effect) :
        self.name = name
        self.effect = effect
    
    def __str__(self):
        return f"{self.name} (Effect: {self.effect})"
    
class healing_potion(items) :
    def __init__(self, size, healing_power) :
        super().__init__(f"{size} Healing potion", f"Restore {healing_power} hp")
        self.size = size
        self.healing_power = healing_power

    def heal(self, target) :
        if (target.max_hp - target.hp) < self.healing_power :
            target.hp += target.max_hp - target.hp
            print(f"You restored {target.max_hp - target.hp} hp")
        else :
            target.hp += self.healing_power
            print(f"You restored {self.healing_power} hp")
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}"
