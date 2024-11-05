from weapons import all_weapons
from items import healing_potion
import msvcrt
import time
from caracters import hero

Potion = healing_potion("Medium",50)
Grosse_Potion = healing_potion("Big", 80)
all_items = [Potion, Grosse_Potion]
Me = hero("Raphael", all_weapons, all_items)

Me.afficher_inventaire()

"""def fight(monster):
    max_hp = monster.hp
    max_hp_hero = Me.hp
    while monster.hp > 0 and Me.hp > 0:
        
        print("Choose your move:")
        time.sleep(0.5)
        if len(all_weapons) > 1 :
            print("1. Attack with", all_weapons[0].name)
            time.sleep(0.1)
            print("2. Attack with", all_weapons[1].name)
            time.sleep(0.1)
            print("3. Inventory")
            time.sleep(0.1)
            print("4. Run")
            print("\n")
            
            touche = msvcrt.getch().decode('utf-8')

            if touche == '1':
                Me.attack = all_weapons[0].damage
                damage_before = monster.hp
                Me.attacking(monster)
                damage_done = damage_before - monster.hp
                print(f"You chose to attack {monster.name} with {all_weapons[0].name}.")
                time.sleep(1.5)
                print(f"You did {damage_done} damage")
                time.sleep(1.5)
                print(f"{monster.name} has {monster.hp} left")
                time.sleep(1.5)

            elif touche == '2':
                Me.attack = all_weapons[1].damage
                damage_before = monster.hp
                Me.attacking(monster)
                damage_done = damage_before - monster.hp
                print(f"You chose to attack {monster.name} with {all_weapons[1].name}.")
                time.sleep(1.5)
                print(f"You did {damage_done} damage.")
                time.sleep(1.5)
                print(f"{monster.name} has {monster.hp} left")
                time.sleep(1.5)
            
            elif touche == '3':
                print("Opening inventory...")

            elif touche == '4':
                print("You chose to run away!")
                break
        else :
            print("1. Attack with", all_weapons[0].name)
            time.sleep(0.1)
            print("3. Inventory")
            time.sleep(0.1)
            print("4. Run")
            print("\n")
            
            touche = msvcrt.getch().decode('utf-8')

            if touche == '1':
                Me.attack = all_weapons[0].damage
                damage_before = monster.hp
                Me.attacking(monster)
                damage_done = damage_before - monster.hp
                print(f"You chose to attack {monster.name} with {all_weapons[0].name}.")
                time.sleep(1.5)
                print(f"You did {damage_done} damage")
                time.sleep(1.5)
                print(f"{monster.name} has {monster.hp} left")
                time.sleep(1.5)

            elif touche == '3':
                print("Opening inventory...")

            elif touche == '4':
                print("You chose to run away!")
                break
        
        if monster.hp <= 0:
            print(f"You defeated {monster.name}!")
            monster.hp = max_hp
            Me.hp = max_hp_hero
            break

        damage_before = Me.hp
        monster.attacking(Me)
        print(f"{monster.name} attack you.")
        time.sleep(1.5)
        print(f"you lost", damage_before - Me.hp,"hp.")
        time.sleep(1.5)
        print(f"you have {Me.hp}hp left")
        print("\n")
        time.sleep(1.5)

        if Me.hp <= 0:
            print("You were defeated...")
            monster.hp = max_hp
            Me.hp = max_hp_hero
            break"""

            
