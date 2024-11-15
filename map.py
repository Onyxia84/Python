import os
import random
from caracters import allcaracters  # Import all characters
from fight import fight  # Import the fight function
from fight import Me  # Import the player (Me) instance
from weapons import all_weapons  # Import all weapons
from items import all_items  # Import all items

# Game maps (grid-based representation)
map_data1 = [
    "##########################",
    "#......................W.#",
    "#........................#",
    "#..P....................._",
    "###########################"
]

map_data2 = [
    "##########################",
    "#P.......................#",
    "#........................_",
    "#........................#",
    "##########################"
]

map_data3 = [
    "##########################",
    "#P.......................#",
    "#........................_",
    "#........................#",
    "##########################"
]

map_data4 = [
    "#######",
    "#.....#",
    "#P.I.B#",
    "#.....#",
    "#######"
]

# Convert maps into lists of lists for easier manipulation
game_maps = {
    "map1": [list(row) for row in map_data1],
    "map2": [list(row) for row in map_data2],
    "map3": [list(row) for row in map_data3],
    "map4": [list(row) for row in map_data4]
}

# Set the default map to the first one
current_map = "map1"

# Function to place characters randomly on the map
def place_characters_randomly(game_map, character, count):
    # Find empty positions (.)
    empty_positions = [(y, x) for y, row in enumerate(game_map) for x, cell in enumerate(row) if cell == '.']
    
    # Ensure there are enough empty positions
    if len(empty_positions) < count:
        raise ValueError("Not enough empty spaces to place all characters.")
    
    # Randomly select positions
    random_positions = random.sample(empty_positions, count)
    
    # Place the characters on the map
    for y, x in random_positions:
        game_map[y][x] = character

# Function to locate the player's starting position
def find_player(game_map):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == 'P':  # Player is represented by 'P'
                return y, x

# Function to display the map
def display_map(game_map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in game_map:
        print("".join(row))

# Function to move the player on the map
def move_player(game_map, player_y, player_x, direction):
    new_y, new_x = player_y, player_x

    # Calculate the new position based on the direction
    if direction == 'z':       # Move up
        new_y -= 1
    elif direction == 's':     # Move down
        new_y += 1
    elif direction == 'q':     # Move left
        new_x -= 1
    elif direction == 'd':     # Move right
        new_x += 1

    # Check if the move is valid
    if game_map[new_y][new_x] == '.':  # Empty space
        game_map[player_y][player_x] = '.'
        game_map[new_y][new_x] = 'P'
        return new_y, new_x, False, False, None
    elif game_map[new_y][new_x] in ['S', 'F', 'D', 'W', 'B', 'I']:  # Collision with a character
        collided_character = game_map[new_y][new_x]
        game_map[player_y][player_x] = '.'
        game_map[new_y][new_x] = 'P'
        return new_y, new_x, True, False, (new_y, new_x, collided_character)
    elif game_map[new_y][new_x] == '_':  # Teleportation tile
        return new_y, new_x, False, True, None

    return player_y, player_x, False, False, None

# Main game loop
def main():
    global current_map  # Allow changing the current map

    # Place characters randomly on maps
    place_characters_randomly(game_maps["map1"], 'S', 5)
    place_characters_randomly(game_maps["map2"], 'F', 6)
    place_characters_randomly(game_maps["map2"], 'W', 1)
    place_characters_randomly(game_maps["map3"], 'D', 7)
    place_characters_randomly(game_maps["map1"], 'I', 2)
    place_characters_randomly(game_maps["map2"], 'I', 2)
    place_characters_randomly(game_maps["map3"], 'I', 1)
    place_characters_randomly(game_maps["map3"], 'W', 1)

    # Locate the player's starting position
    player_y, player_x = find_player(game_maps[current_map])

    # Game loop
    while True:
        # Display the map
        display_map(game_maps[current_map])

        # Prompt the player for movement
        print("\nMove (z: up, s: down, q: left, d: right, i: inventory, x: quit)")
        move = input("Your move: ").lower()

        # Quit the game
        if move == 'x':
            Me.display_inventory()
            print("Goodbye!")
            break

        # Show inventory
        if move == 'i':
            Me.display_inventory()  # Display inventory
            input("\nPress Enter to continue...")
            continue

        # Move the player
        if move in ['z', 's', 'q', 'd']:
            player_y, player_x, collided, teleported, collision_data = move_player(
                game_maps[current_map], player_y, player_x, move
            )
            
            # Handle collision with a character
            if collided and collision_data:
                collision_y, collision_x, character = collision_data
                display_map(game_maps[current_map])

                # Different characters trigger specific events
                if character == 'S':  # Skeleton
                    print("\nYou encountered a Skeleton! Get ready for battle!")
                    if not fight(allcaracters[0], Me.inventory["weapons"], Me.inventory["items"]):
                        print("Game Over. You lost the battle!")
                        break
                elif character == 'F':  # Falmer
                    print("\nYou encountered a Falmer! Get ready for battle!")
                    if not fight(allcaracters[1], Me.inventory["weapons"], Me.inventory["items"]):
                        print("Game Over. You lost the battle!")
                        break
                elif character == 'D':  # Dragon
                    print("\nYou encountered a Dragon! Get ready for battle!")
                    if not fight(allcaracters[2], Me.inventory["weapons"], Me.inventory["items"]):
                        print("Game Over. You lost the battle!")
                        break
                elif character == 'B':  # Boss
                    print("\nYou encountered the Boss! Get ready for battle!")
                    if not fight(allcaracters[3], Me.inventory["weapons"], Me.inventory["items"]):
                        print("Game Over. You lost the battle!")
                        break
                    print("Congratulations! You completed the game!")
                    break
                elif character == 'W':  # Weapon tile
                    if current_map == "map1":
                        Me.take_weapons(all_weapons[1])
                    elif current_map == "map2":
                        Me.take_weapons(all_weapons[2])
                    elif current_map == "map3":
                        Me.take_weapons(all_weapons[3])
                elif character == 'I':  # Item tile
                    if current_map == "map1":
                        Me.take_item(all_items[1])
                    elif current_map == "map2":
                        Me.take_item(all_items[2])
                    elif current_map == "map3":
                        Me.take_item(all_items[3])
                    elif current_map == "map4":
                        Me.take_item(all_items[4])

                # Remove the character from the map after the event
                game_maps[current_map][collision_y][collision_x] = 'P'

                input("Press Enter to continue...")

            # Handle teleportation
            if teleported:
                if current_map == "map1":
                    current_map = "map2"
                elif current_map == "map2":
                    current_map = "map3"
                elif current_map == "map3":
                    current_map = "map4"

                # Update the map and player's position
                player_y, player_x = find_player(game_maps[current_map])

# Start the game
if __name__ == "__main__":
    main()
