from weapons import all_weapons  # Import all weapons from the weapons module
from items import all_items  # Import all items from the items module
import msvcrt  # Module for keyboard input in Windows
import random  # Module for generating random numbers
import time  # Module for handling time-related tasks
from caracters import hero  # Import the 'hero' class from the characters module

# Initialize the player's inventory with one weapon and one item
items = [all_items[0]]
weapons = [all_weapons[0]]
Me = hero("Raphael", weapons, items)  # Create the main player character with the name Raphael

# Combat function between the player and a monster
def fight(monster, weapons, inventory):
    max_hp = monster.hp  # Save the monster's max health for resetting later
    base_defense = Me.defense  # Save the player's base defense for resetting later

    # Continue combat as long as both the player and monster are alive
    while monster.hp > 0 and Me.hp > 0:
        print("Choose your move:")  # Prompt the player for an action
        time.sleep(0.5)

        # Display combat options based on the number of weapons the player has
        if len(Me.inventory["weapons"]) > 1:
            print("1. Attack with", weapons[0].name)  # Option to attack with the first weapon
            time.sleep(0.1)
            print("2. Attack with", weapons[1].name)  # Option to attack with the second weapon
            time.sleep(0.1)
            print("3. Inventory")  # Option to open the inventory
            time.sleep(0.1)
            print("\n")
            
            # Capture the player's input
            touche = msvcrt.getch().decode('utf-8')

            if touche == '1':
                # Attack with the first weapon
                print(f"You chose to attack {monster.name} with {weapons[0].name}.")
                if random.randrange(0, 100, 1) >= weapons[0].miss_rate:
                    # Successful attack logic
                    Me.attack += weapons[0].damage  # Temporarily increase the player's attack
                    damage_before = monster.hp
                    Me.attacking(monster)  # Perform the attack on the monster
                    damage_done = damage_before - monster.hp
                    time.sleep(0.75)
                    print(f"You did {damage_done} damage")
                    time.sleep(0.75)
                    print(f"{monster.name} has {monster.hp} HP left")
                    time.sleep(0.75)
                    Me.attack -= weapons[0].damage  # Restore the player's attack stat
                else:
                    # Missed attack logic
                    time.sleep(0.75)
                    print("Attack missed")
                    time.sleep(0.75)

            elif touche == '2':
                # Attack with the second weapon
                print(f"You chose to attack {monster.name} with {weapons[1].name}.")
                if random.randrange(0, 100, 1) >= weapons[1].miss_rate:
                    # Successful attack logic
                    Me.attack += weapons[1].damage
                    damage_before = monster.hp
                    Me.attacking(monster)
                    damage_done = damage_before - monster.hp
                    time.sleep(0.75)
                    print(f"You did {damage_done} damage")
                    time.sleep(0.75)
                    print(f"{monster.name} has {monster.hp} HP left")
                    time.sleep(0.75)
                    Me.attack -= weapons[1].damage
                else:
                    # Missed attack logic
                    time.sleep(0.75)
                    print("Attack missed")
                    time.sleep(0.75)
            
            elif touche == '3':
                # Open the inventory
                print("Opening inventory...")
                if inventory_in_fight(inventory):  # Check if the inventory action is complete
                    continue
                print("\n")
            else:
                # Invalid input
                print("Wrong input, please retry")
                continue

        else:
            # Logic when the player has only one weapon
            print("1. Attack with", weapons[0].name)
            time.sleep(0.1)
            print("3. Inventory")
            time.sleep(0.1)
            print("\n")
            
            touche = msvcrt.getch().decode('utf-8')

            if touche == '1':
                # Attack with the only weapon available
                print(f"You chose to attack {monster.name} with {weapons[0].name}.")
                if random.randrange(0, 100, 1) >= weapons[0].miss_rate:
                    Me.attack += weapons[0].damage
                    damage_before = monster.hp
                    Me.attacking(monster)
                    damage_done = damage_before - monster.hp
                    time.sleep(0.75)
                    print(f"You did {damage_done} damage")
                    time.sleep(0.75)
                    print(f"{monster.name} has {monster.hp} HP left")
                    time.sleep(0.75)
                    Me.attack -= weapons[0].damage
                else:
                    time.sleep(0.75)
                    print("Attack missed")
                    time.sleep(0.75)

            elif touche == '3':
                # Open the inventory
                print("Opening inventory...")
                if inventory_in_fight(inventory):
                    continue
                print("\n")
            else:
                print("Wrong input, please retry")
                continue
        
        # Check if the monster is defeated
        if monster.hp <= 0:
            print(f"You defeated {monster.name}!")
            Me.defense = base_defense  # Restore the player's defense stat
            monster.hp = max_hp  # Restore the monster's health
            xp_won = monster.level * 25  # Calculate experience points won
            Me.xp_bar += xp_won
            print(f"You won {xp_won} XP, now at {Me.xp_bar}/{Me.xp_needed} XP to reach the next level.")
            if Me.xp_bar >= Me.xp_needed:
                Me.level_up()  # Level up the player
            Me.hp = Me.max_hp  # Restore the player's health
            return True

        # Monster's turn to attack
        damage_before = Me.hp
        monster.attacking(Me)  # Monster attacks the player
        print(f"{monster.name} attacked you.")
        time.sleep(0.75)
        print(f"You lost {damage_before - Me.hp} HP.")
        time.sleep(0.75)
        print(f"You have {Me.hp} HP left.")
        print("\n")
        time.sleep(0.75)

        # Check if the player is defeated
        if Me.hp <= 0:
            print("You were defeated...")
            monster.hp = max_hp
            Me.hp = Me.max_hp
            return False


# Inventory management during combat
def inventory_in_fight(inventory):
    while True:
        print("What do you want to do?")
        print("Your inventory:")
        
        # Display all items in the inventory
        for idx, item in enumerate(inventory):
            print(f"{idx}. {item.name}")
        
        print("Type the ID of the item you want to use or type 'leave' to exit the inventory.")
        
        user_input = input("Your choice: ")
        
        if user_input.lower() == "leave":
            print("Leaving inventory.")
            return True

        if user_input.isdigit():
            item_id = int(user_input)
            
            if 0 <= item_id < len(inventory):
                item = inventory[item_id]
                
                if hasattr(item, 'use'):
                    item.use(Me)  # Use the item on the player
                    print(f"You used {item.name}.")
                    del inventory[item_id]  # Remove the item after use
                    return False
                else:
                    print(f"{item.name} cannot be used in this way.")
            else:
                print("Invalid ID, please try again.")
        else:
            print("Invalid input, please enter a valid ID or 'leave'.")
