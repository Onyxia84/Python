# Base class for all characters
class caracters():
    def __init__(self, name, attack, defense, hp, level):
        # Initialize character attributes
        self.name = name  # Name of the character
        self.attack = attack  # Attack strength
        self.defense = defense  # Defense value
        self.hp = hp  # Current health points
        self.level = level  # Character level
        self.max_hp = hp  # Maximum health points

    # Method for attacking another character
    def attacking(self, target):
        if self.attack > target.defense:  # If attack exceeds target's defense
            target.hp -= self.attack - target.defense  # Subtract the difference from target's health
        else:
            target.hp -= 1  # Minimum damage is 1 even if defense is higher

# Hero class, inheriting from the caracters class
class hero(caracters):
    def __init__(self, name, weapons, items):
        super().__init__(name, 0, 10, 60, 1)  # Initialize with default stats
        self.xp_bar = 0  # Current experience points
        self.xp_needed = 100  # XP needed to level up
        self.inventory = {  # Hero's inventory containing weapons and items
            "weapons": weapons,
            "items": items
        }

    # Method for leveling up the hero
    def level_up(self):
        self.attack += 10  # Increase attack
        self.defense += 10  # Increase defense
        self.max_hp += 30  # Increase max health points
        self.level += 1  # Increase level
        self.xp_bar -= self.xp_needed  # Reduce XP bar by the amount needed for leveling up
        self.xp_needed += 40  # Increase XP needed for the next level
        print(f"Congratulations! You leveled up and are now level {self.level}")

    # Method to handle taking new weapons
    def take_weapons(self, weapon):
        while True:
            print(f"You found {weapon}! Do you want to take it? (y/n)")
            choice = input().strip().lower()  # Get player input

            if choice == 'y':
                # Check if weapon inventory is full (max 2 weapons)
                if len(self.inventory["weapons"]) >= 2:
                    print("You can't carry more than 2 weapons. Do you want to replace one of yours? (y/n)")
                    replace_choice = input().strip().lower()

                    if replace_choice == 'y':
                        # Show current weapons
                        print("Your current weapons:")
                        current_weapons = self.afficher_weapons()

                        # Ask which weapon to replace
                        print("Which one do you want to replace? Enter the number (0 or 1):")
                        try:
                            weapon_to_replace = int(input().strip())
                            if weapon_to_replace in range(len(current_weapons)):
                                # Replace weapon
                                removed_weapon = self.inventory["weapons"].pop(weapon_to_replace)
                                self.inventory["weapons"].append(weapon)
                                print(f"You replaced {removed_weapon} with {weapon}.")
                                break
                            else:
                                print("Invalid choice. Please select a valid weapon number.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    elif replace_choice == 'n':
                        print("You decided not to take the weapon.")
                        break
                    else:
                        print("Invalid choice. Please type 'y' or 'n'.")
                else:
                    # Add the weapon if there's space
                    self.inventory["weapons"].append(weapon)
                    print(f"You took the {weapon}.")
                    break
            elif choice == 'n':
                print("You decided not to take the weapon.")
                break
            else:
                print("Invalid choice. Please type 'y' or 'n'.")

    # Method to add an item to the inventory
    def take_item(self, item):
        print(f"You found {item}! It has been added to your inventory.")
        self.inventory["items"].append(item)

    # Display the full inventory
    def afficher_inventaire(self):
        print("Inventory:")
        for category, objects in self.inventory.items():
            print(f"\n{category.capitalize()}:")
            for obj in objects:
                print(f"  - {obj}")

    # Display the list of items
    def afficher_items(self):
        print("Items:")
        for item in self.inventory["items"]:
            print(f"{item}")
        return self.inventory["items"]

    # Display the list of weapons
    def afficher_weapons(self):
        print("Weapons:")
        for id, weapon in enumerate(self.inventory["weapons"]):  # Use enumerate for indexing
            print(f"{id} - {weapon}")
        return self.inventory["weapons"]


# Enemy character examples
skeleton = caracters("Skeleton", 30, 25, 160, 2)  # Skeleton enemy
falmer = caracters("Falmer", 60, 15, 130, 5)  # Falmer enemy
dragons = caracters("Dragons", 100, 110, 280, 10)  # Dragon enemy
Boss = caracters("Boss", 155, 170, 445, 20)  # Boss enemy

# List of all characters
allcaracters = [skeleton, falmer, dragons, Boss]





