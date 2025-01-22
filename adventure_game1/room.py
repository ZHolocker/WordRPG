class Room:
    """
    Represents a room in the adventure game.
    
    Attributes:
        name (str): The name of the room.
        description (str): A brief description of the room.
        exits (dict): A dictionary of exits from the room.
        items (list): A list of items in the room.
        enemies (list): A list of enemies in the room.
    """
    def __init__(self, name, description, exits=None, items=None, enemies=None):
        self.name = name
        self.description = description
        self.exits = exits if exits else {}
        self.items = items if items else []
        self.enemies = enemies if enemies else []

    def describe(self):
        """
        Returns a formatted string describing the room.
        
        """
        description = f"You are in {self.name}. {self.description}"
        items_str = ""
        if self.items:
            items_str = "\n".join([f"- {item}" for item in self.items])
            description += f"\nItems in the room:\n{items_str}"
        else:
            description += "\nThere are no items in this room."
        exits_str = ""
        if self.exits:
            exits_str = "\n".join([f"- {direction}" for direction in self.exits])
            description += f"\nExits:\n{exits_str}"
        return description
    
    