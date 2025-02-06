#DUNGEON FURY : LA LEGENDE DES TERRES OUBLIEES

#Dans un monde ravagé par le chaos et l'oubli, une légende murmure à propos d'un artefact mystique appelé l'Emprise de l'Éternité.
#Cet artefact, perdu dans les profondeurs des Terres Oubliées, est réputé pour donner un pouvoir illimité à celui qui le possède.
#Cependant, ce trésor est gardé par des créatures anciennes et des énigmes mortelles.Toi, un aventurier au cœur vaillant, as été choisi par un oracle mystérieux pour braver ce péril.
#Ton village natal, réduit en cendres par l'invasion des monstres, t’a donné une raison de te battre : vaincre les ténèbres et rétablir l'équilibre dans le royaume.


import random

# *Classes*
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)

    def deal_damage(self, opponent):
        damage = max(self.attack - opponent.defense, 1)
        opponent.take_damage(damage)
        return damage

# *Player Class*
class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=10, defense=5)
        self.inventory = []
        self.xp = 0
        self.level = 1

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 3
        print("Level up! " + self.name + " is now level " + str(self.level) + ".")

    def use_item(self):
        if not self.inventory:
            print("Your inventory is empty!")
            return False
        print("Inventory:")
        for i, item in enumerate(self.inventory):
            print(str(i + 1) + ": " + item)

        try:
            choice = int(input("Choose an item to use (number): ")) - 1
            if 0 <= choice < len(self.inventory):
                item = self.inventory.pop(choice)
                if item == "Crimson Revival":
                    self.hp += 20
                    print("You used a Crimson Revival and restored 20 HP!")
                elif item == "Attack Sword":
                    self.attack += 5
                    print("You used an Attack Sword and gained +5 Attack!")
                elif item == "Defense Shield":
                    self.defense += 5
                    print("You used a Defense Shield and gained +5 Defense!")
                return True
            else:
                print("Invalid choice.")
                return False
        except ValueError:
            print("Invalid input.")
            return False

#*Enemy Class*
class Enemy(Character):
    def __init__(self, name, level):
        hp = 30 + level * 10
        attack = 5 + level * 2
        defense = 3 + level
        super().__init__(name, hp, attack, defense)

#*Fights*

# Des Décisions à Chaque Étape :
# À travers des choix stratégiques (attaquer, utiliser des objets ou fuir), tu forgerras ton destin. Chaque décision te rapprochera du triomphe ou te mènera à une fin tragique.
# Le royaume compte sur toi pour retrouver la lumière et marquer ton nom parmi les héros des Terres Oubliées.

def battle(player, enemy):
    print("A wild " + enemy.name + " appears!")
    while player.is_alive() and enemy.is_alive():
        print(player.name + ": " + str(player.hp) + " HP | " + enemy.name + ": " + str(enemy.hp) + " HP")
        action = input("Do you want to (A)ttack, (I)nventory, or (R)un? ").lower()
        if action == 'a':
            damage = player.deal_damage(enemy)
            print("You dealt " + str(damage) + " damage to the " + enemy.name + ".")
            if enemy.is_alive():
                enemy_damage = enemy.deal_damage(player)
                print("The " + enemy.name + " dealt " + str(enemy_damage) + " damage to you.")
        elif action == 'i':
            if not player.use_item():
                print("You lost your turn!")
        elif action == 'r':
            print("You ran away!")
            return False
        else:
            print("Invalid action.")
            continue  # *Continue pour passer à l'itération suivante de la boucle si l'action est invalide*

    if player.is_alive():
        print("You defeated the " + enemy.name + "!")
        player.xp += 20
        if player.xp >= 100:
            player.level_up()
        return True
    else:
        print("You were defeated...")
        return False

# Départ de l'Aventure
# Tu commences ton périple dans une plaine brumeuse. L'Oracle t'a offert une épée rouillée, symbole de ton destin naissant, et t'a mis en garde :
# "Chaque bataille te rapprochera de l'artefact, mais méfie-toi. Les Terres Oubliées testent autant le courage que l'esprit."
# Ton premier objectif est d'explorer les environs pour trouver des indices et te renforcer. Mais chaque pas te rapproche des abîmes du désespoir, où les monstres rôdent dans l'ombre.

def explore(player):
    print("You are investigating the area...")
    if random.choice([True, False]):

# Les Monstres et leurs Histoires
# Cacazo - Une créature reptilienne qui aime tendre des embuscades. Il était autrefois un garde royal, maudit pour sa trahison envers son roi.
# Haywayer - Un fantôme armé d'une faux. Ce guerrier spectral hante les ruines pour venger son armée décimée.
# Dauwag - Une bête imposante, protectrice des trésors maudits. Certains disent qu'elle est la clé pour accéder à l'antre final.

        enemy = Enemy(random.choice(["Cacazo", "Haywayer", "Dauwag"]), player.level)
        battle(player, enemy)

# Progression et Découvertes
# En explorant, tu trouveras des artefacts anciens tels que :
# Crimson Revival : Une potion rare distillée à partir de l'énergie des âmes.
# Épée d'Attaque : Un fragment d'une lame légendaire, brisée lors de la Grande Guerre.
# Bouclier Défensif : Un bouclier enchanté qui appartenait à un roi oublié.
# Les objets ne sont pas uniquement des aides au combat, mais aussi des morceaux d'histoire du royaume.

    else:
        item = random.choice(["Crimson Revival", "Attack sword", "Defense Shield"])
        player.inventory.append(item)
        print("You found a " + item + "!")

#*Main Game lobby*
def main():
    print("Welcome to the Dungeon Fury !")
    name = input("Enter your character's name: ")
    player = Player(name)

#*Gameplay*
    while player.is_alive():
        print("Options: (S)cout, (I)nventory, (Q)uit")
        choice = input("What do you want to do? ").lower()

        if choice == 's':
            explore(player)
        elif choice == 'i':
            print("Inventory:")
            if not player.inventory:
                print("Your inventory is empty.")
            else:
                for item in player.inventory:
                    print("- " + item)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# Le But Ultime :
# Ton aventure t'amènera finalement à la Forteresse des Ombres, où repose l'Emprise de l'Éternité. Là-bas, tu affronteras le Maître des Ténèbres, une entité millénaire.
# Mais attention : seuls les aventuriers qui ont prouvé leur valeur en atteignant le niveau 5 peuvent espérer le vaincre.

