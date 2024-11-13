class caracters() :
    def __init__(self, name, attack, defense, hp, level):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.level = level
        self.max_hp = hp

    def attacking(self, target) :
        if self.attack > target.defense :
            target.hp -= self.attack - target.defense
        else :
            target.hp -= 1
    
class hero(caracters):
    def __init__(self, name, weapons, items):
        super().__init__(name, 0, 10, 100, 5)
        self.inventory = {
            "weapons": weapons,
            "items": items
        }

    def afficher_inventaire(self):
        print("Inventaire :")
        for categorie, objets in self.inventory.items():
            print(f"\n{categorie.capitalize()}:")
            for objet in objets:
                print(f"  - {objet}")

    def afficher_items(self):
        print("Items:")
        for item in self.inventory["items"]:
            print(f"{item}")
        return self.inventory["items"]


class dragon(caracters) :
    def __init__(self, name, attack_name, capacity_name) :
        super().__init__(name, 200, 50, 100, 20)
        self.attack_name = attack_name
        self.capacity_name = capacity_name

    def capacity(self) :
        self.hp += 50
        print(self.name, "utilise", self.capacity_name, self.name, "recupere 50 hp")
        
falmer = caracters("Falmer", 60, 50, 90, 13)
skeleton = caracters("Skeleton", 35, 25, 160, 5)

allcaracters = [falmer, skeleton]




