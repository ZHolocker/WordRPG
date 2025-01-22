from room import Room
from items import *

#This is to define all the character class and functions and attributes that belong to it
#I am hoping to make an NPC class as well, that way they can interact with the player


class Character:
    def __init__(self, name, hp, shield, type, attack, defense, magic, intelligence, gold) -> None:
        self.name = name
        self.hp = hp
        self.shield = shield
        self.type = type
        self.inventory = []
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.intelligence = intelligence
        self.gold = gold


    def damage_taken(self):
        damage = 10
        if self.hp > 0:
            self.hp -= damage
            if self.hp <= 0:
                print(f"{self.name} has fallen in battle!")
            else:
                print(f"{self.name} takes {damage} damage!")
        

    def show_health(self):
        print(f"You have {self.hp} hp left. Be careful out there!")
    
    def show_stats(self):
        print(f"Attack: {self.attack}, Defense: {self.defense}, Magic: {self.magic}, Health: {self.hp}, Intelligence: {self.intelligence}, Gold: {self.gold}")

    def pick_up(self, item_name, room):
    for item in room.items:
        if item.name == item_name and item not in self.inventory:
            self.inventory.append(item)
            room.items.remove(item)
            print(f"You have picked up the {item_name}.")
            return  # exit the function after picking up the item
    print(f"There is no {item_name} here to pick up.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("You are not carrying anything.")

    def update_stats(self):
        for item in self.inventory:
            if 'effects' in item:
                for stat, value in item['effects'].items():
                    if stat == 'Attack':
                        self.attack += value
                    elif stat == 'Defense':
                        self.defense += value
                    elif stat == 'Magic':
                        self.magic += value
                    elif stat == 'Intelligence':
                        self.intelligence += value
                    elif stat == 'Health':
                        self.hp += value
                    elif stat == 'Shield':
                        self.shield += value
                    elif stat == 'Gold':
                        self.gold += value
                    elif stat is None:
                        pass
                    else:
                        print("Invalid stat type.")
                        

class NPC(Character):
    def __init__(self, name, hp, shield, type, attack, defense, magic, intelligence, gold) -> None:
        super().__init__(name, hp, shield, type, attack, defense, magic, intelligence, gold)
        self.inventory = []
        self.experience = 0
        self.level = 1
        self.storyline = None

    def level_up(self):
        self.level += 1
        self.attack += 10
        self.defense += 15
        self.magic += 10
        self.intelligence += 8
        self.gold += 10
        self.experience = 0
        print(f"Congratulations! You have leveled up to level {self.level}!")
    
