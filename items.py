# Base class for items in the game
class Items:
    def __init__(self, name, effect):
        self.name = name  # Name of the item
        self.effect = effect  # Description of the item's effect
    
    # String representation of the item
    def __str__(self):
        return f"{self.name} (Effect: {self.effect})"

# Subclass representing healing potions
class HealingPotion(Items):
    def __init__(self, size, healing_power):
        # Initialize with name and effect based on size and healing power
        super().__init__(f"{size} Healing Potion", f"Restore {healing_power} HP")
        self.size = size  # Size of the potion (e.g., Small, Medium, Big)
        self.healing_power = healing_power  # Amount of HP restored by the potion

    # Use the potion on a target (typically a character)
    def use(self, target):
        # If the target's missing HP is less than the potion's healing power
        if (target.max_hp - target.hp) < self.healing_power:
            restored_hp = target.max_hp - target.hp
            target.hp += restored_hp  # Restore up to the max HP
            print(f"You restored {restored_hp} HP")
            del self  # Remove the potion after use
        else:
            target.hp += self.healing_power  # Restore the potion's full healing power
            print(f"You restored {self.healing_power} HP")
    
    # String representation of the healing potion
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}"

# Subclass representing defensive potions
class DefensivePotion(Items):
    def __init__(self, size, defense_power):
        # Initialize with name and effect based on size and defense power
        super().__init__(f"{size} Defensive Potion", f"Increases your defense by {defense_power}")
        self.size = size  # Size of the potion (e.g., Medium, Big)
        self.defense_power = defense_power  # Amount of defense increased by the potion
    
    # Use the potion on a target (typically a character)
    def use(self, target):
        target.defense += self.defense_power  # Increase the target's defense stat

    # String representation of the defensive potion
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}"

# Create instances of healing potions with different sizes and healing powers
Potion = HealingPotion("Small", 50)
Medium_Potion = HealingPotion("Medium", 80)
Big_Potion = HealingPotion("Big", 100)

# Create instances of defensive potions with different sizes and defense powers
Medium_Defense_Potion = DefensivePotion("Medium", 10)
Big_Defense_Potion = DefensivePotion("Big", 25)

# List containing all items for easy reference
all_items = [Potion, Medium_Potion, Medium_Defense_Potion, Big_Potion, Big_Defense_Potion]
