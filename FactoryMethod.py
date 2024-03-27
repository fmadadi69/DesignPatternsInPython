from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass


class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self):
        print(f"""
                Warrior name: {self.name}
                health level: {self.health}
                strength: {self.strength}
                Attacks with: Sword
                """)


class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self):
        print(f"""
                Mage name: {self.name}
                health level: {self.health}
                mana: {self.mana}
                Attacks with: Spell
                """)


class Archer(Character):
    def __init__(self, name, health, accuracy):
        super().__init__(name, health)
        self.accuracy = accuracy

    def attack(self):
        print(f"""
                Archer name: {self.name}
                health level: {self.health}
                accuracy: {self.accuracy}
                Attacks with: Arrows
                """)

# ########### FACTORY METHOD ############# #


class CharacterCreator(ABC):
    @abstractmethod
    def create_character(self, name, health):
        pass


class WarriorCreator(CharacterCreator):
    def create_character(self, name, health):
        return Warrior(name, health, strength=20)


class MageCreator(CharacterCreator):
    def create_character(self, name, health):
        return Mage(name, health, mana=10)


class ArcherCreator(CharacterCreator):
    def create_character(self, name, health):
        return Archer(name, health, accuracy=100)


# ############# CLIENT CODE ############## #
player_name = str(input("Enter your character's name:"))
player_health = int(input("Enter your character's health:"))
player_choice = str(input("Choose your character's type (Warrior - Mage - Archer):"))
creator = None

if player_choice == 'Warrior':
    creator = WarriorCreator()
elif player_choice == 'Mage':
    creator = MageCreator()
elif player_choice == 'Archer':
    creator = ArcherCreator()
else:
    player_choice = str(input("Invalid Character type. Choose your character's type (Warrior - Mage - Archer) AGAIN:"))

if creator:
    character = creator.create_character(player_name, player_health)
    character.attack()





