import os
import random
from caracters import allcaracters
from fight import fight

# Cartes du jeu
map_data1 = [
    "##########################",
    "#........................#",
    "#........................#",
    "#..P....................._",
    "###########################"
]

map_data2 = [
    "##########################",
    "#P.......................#",
    "#........................#",
    "_........................#",
    "##########################"
]

# Convertir les cartes en listes de listes
game_maps = {
    "map1": [list(row) for row in map_data1],
    "map2": [list(row) for row in map_data2]
}

# Activer la première carte par défaut
current_map = "map1"

# Fonction pour ajouter des personnages à des positions aléatoires
def place_characters_randomly(game_map, character, count):
    # Trouver les positions vides (.)
    empty_positions = [(y, x) for y, row in enumerate(game_map) for x, cell in enumerate(row) if cell == '.']
    
    # Vérifier s'il y a suffisamment de cases vides
    if len(empty_positions) < count:
        raise ValueError("Pas assez de cases vides pour placer tous les personnages.")
    
    # Choisir des positions aléatoires
    random_positions = random.sample(empty_positions, count)
    
    # Placer les personnages sur la carte
    for y, x in random_positions:
        game_map[y][x] = character

# Trouver la position initiale du joueur
def find_player(game_map):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == 'P':
                return y, x

# Afficher la carte
def display_map(game_map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Nettoie la console
    for row in game_map:
        print("".join(row))

# Déplacer le joueur
def move_player(game_map, player_y, player_x, direction):
    new_y, new_x = player_y, player_x

    # Déterminer la nouvelle position
    if direction == 'z':       # Haut
        new_y -= 1
    elif direction == 's':     # Bas
        new_y += 1
    elif direction == 'q':     # Gauche
        new_x -= 1
    elif direction == 'd':     # Droite
        new_x += 1

    # Vérifier si le mouvement est valide
    if game_map[new_y][new_x] == '.':  # Case vide
        game_map[player_y][player_x] = '.'
        game_map[new_y][new_x] = 'P'
        return new_y, new_x, False, False
    elif game_map[new_y][new_x] == 'I':  # Collision avec un personnage
        game_map[player_y][player_x] = '.'
        game_map[new_y][new_x] = 'P'
        return new_y, new_x, True, False
    elif game_map[new_y][new_x] == '_':  # Collision avec une case de téléportation
        return new_y, new_x, False, True

    return player_y, player_x, False, False

# Jeu principal
def main():
    global current_map  # Permet de changer de carte

    # Ajouter des personnages (I) à des positions aléatoires sur la carte actuelle
    place_characters_randomly(game_maps[current_map], 'I', 1)

    # Trouver la position initiale du joueur
    player_y, player_x = find_player(game_maps[current_map])

    # Boucle de jeu
    while True:
        # Afficher la carte
        display_map(game_maps[current_map])

        # Demander le déplacement au joueur
        print("\nDéplacez-vous (z: haut, s: bas, q: gauche, d: droite, x: quitter)")
        move = input("Votre déplacement : ").lower()

        # Quitter le jeu
        if move == 'x':
            print("Au revoir !")
            break

        # Déplacer le joueur
        if move in ['z', 's', 'q', 'd']:
            player_y, player_x, collided, teleported = move_player(
                game_maps[current_map], player_y, player_x, move
            )

            # Si collision avec un personnage
            if collided:
                display_map(game_maps[current_map])
                print("\nVous avez rencontré un personnage (I) ! Préparez-vous au combat !")
                fight(allcaracters[1])  # Déclenche la fonction fight
                input("Appuyez sur Entrée pour continuer...")

            # Si le joueur est téléporté
            if teleported:
                if current_map == "map1":
                    current_map = "map2"  # Passer à la deuxième carte
                elif current_map == "map2":
                    current_map = "map1"  # Retour à la première carte

                # Mettre à jour la nouvelle carte et positionner le joueur
                player_y, player_x = find_player(game_maps[current_map])

# Lancer le jeu
if __name__ == "__main__":
    main()
