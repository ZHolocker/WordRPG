from character import *
from room import *


# this is where I keep the storylines of the game as it all unfolds I will call each storyline as the story unfolds.
def player_greeting(player):
    greet = (
        f"Welcome {player.name}, destiny has called you to this adventure. You see, this world "
        f"is in trouble. There is a terrible threat that is about to strike. You must save the world from this threat. "
        f"You are a {player.type} and have {player.hp} health points. This adventure starts off in a mystery building. "
        f"Feel free to collect things on your way through. Some things may be dangerous, while others helpful to you. "
        f"This is the story of how you, the unexpected {player.type}, began your quest to save the world."
    )
    return greet

