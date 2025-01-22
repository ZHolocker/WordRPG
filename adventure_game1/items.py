from character import *
#I am creating the items here for the character to interact with


class Item:
    def __init__(self, name, description, effect=None):
        self.name = name
        self.description = description
        self.effect = effect

#creating the items for rooms

sword : Item = Item("Sword", "A sharp sword", effect={"Attack": 1})
shield : Item = Item("Shield", "A heavy shield", effect={"Defense": 2})
Old_book : Item = Item("Old Book", "An old book", effect={"Intelligence": 1})
Book_of_magic : Item = Item("Book of magic", "A book of magic", effect={"Magic": 2})
Rusty_keys: Item = Item("Rusty Keys", "Rusty keys", effect={None})
gold: Item = Item("Gold", "Gold", effect={"Gold": 20})
torch: Item = Item("Torch", "A torch", effect={None})
broken_mirror: Item = Item("Broken Mirror", "A broken mirror", effect={"Health": -20})

#creating the items for shops
potion: Item = Item("Potion", "A healing potion", effect={"Health": 20})
mega_potion: Item = Item("Mega Potion", "A mega healing potion", effect={"Health": 50})
antidote: Item = Item("Antidote", "An antidote", effect={"Health": 100})
#This next potion will allow the player to level up, but need to work on that process of leveling up with an item
level_up_potion: Item = Item("Level Up Potion", "A potion that allows you to level up", effect={"Health": 100})

