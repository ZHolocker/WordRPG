from character import *
from room import Room
from items import *
from storyline import *

def main():
    # Initialize player
    player = Character('Zachary', hp=100, shield=100, type="wizard", attack=10, defense=5, magic=20, intelligence=10, gold=100)
    print(f"Congrats {player.name}, you are now a {player.type}!!")
    print(player.show_stats())
    print(player_greeting(player))
    
    # Define rooms
    first_room = Room(
        name="The Beginning",
        description="""This is the room where your adventure begins. There is a faint light coming from the north.""",
        exits={"north": second_room},
        items=["Old book", "Rusty key", "candle", "sword"],
        enemies=[]
    )
    
    second_room = Room(
        name="The second room",
        description="You enter a dark hallway. The air smells musty and old.",
        exits={"south": first_room, "east": third_room},
        items=["Torch", "Broken mirror"],
        enemies=[]
    )
    
    third_room = Room(
        name="The final room",
        description="You have reached the end of the hallway. It is dark and empty.",
        exits={"west": second_room, "north": outside_area1},
        items=["Gold"],
        enemies=[]
    )
    
    outside_area1 = Room(
        name="Outside area 1",
        description="You have reached the end of the hallway. It is dark and empty.",
        exits={"south": third_room, "west": second_room},
        items=["Torch"],
        enemies=[]
    )
    
    # Link rooms
    first_room.exits["north"] = second_room
    
    current_room = first_room
    
    # Game loop
    while True:
        command = input("\nWhat would you like to do? (Move, pick up, inventory)").lower()
        
        if command in current_room.exits:
            current_room = current_room.exits[command]
            print(f"\nYou move {command}.")
            print(current_room.describe())
        
        elif command.startswith("pick up "):
            item = command[8:].strip()
            player.pick_up(item, current_room)
        
        elif command == "inventory":
            player.show_inventory()
        
        else:
            print("Invalid command. Try again.")




if __name__ == "__main__":
    main()
