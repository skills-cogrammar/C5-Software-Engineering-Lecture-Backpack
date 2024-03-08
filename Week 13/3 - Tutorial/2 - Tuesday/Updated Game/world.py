from random import choice, randint
from characters import Character, Warrior, Archer, Zombie, Goblin
from items import *

class Room:
    """
    Object representing a Room that will contain obejcts for the player to interact with.
    
    Attributes:
    items : Item - Items available to spawn in room.
    enemies : Character - Enemies available to spawn in room.
    __obj - Current object in room.
    """
    items = [Health, HeartBox]
    enemies = [Zombie, Goblin]

    def __init__(self):
        self.__obj = choice(self.items+self.enemies)() # Parenthesis to execute construtor

    def get_object(self):
        """Returns object present in room."""
        return self.__obj
    
    def __str__(self) -> str:
        """Returns a string representation of the Room object."""
        return f"This room contains a {self.__obj}"
    

class World:
    """
    Class representing the in-game world where the player will be interacting
    with rooms that contain objects.
    
    Attributes:\n
    classes : dict - Dictionary containing all the potential classes for the player.
    __player : Player - Player character in the world.
    max_level : int - Maximum amount a rooms a player can enter before the game ends.
    current_level : int - The current room the player in entering.
    rooms : Room - The available rooms for the player to enter.
    """
    classes = {
        "w" : Warrior,
        "a" : Archer
        }

    def __init__(self, max_level):
        self.__player = None
        self.max_level = max_level
        self.current_level = 0
        self.rooms = []

    def set_player(self, class_type):
        """Set the player character to the given class type."""
        if class_type in self.classes:
            self.__player = self.classes[class_type]() # Parenthesis to execute construtor
        else:
            raise KeyError("Class key not found.")
        
    def get_player(self):
        """Get the current player character."""
        return self.__player

    def __generate_rooms(self):
        """Generate the rooms for the current level."""
        self.rooms = [Room() for _ in range(randint(1,5))]

    def next_level(self):
        """Increments the current level attribute and generates a new set of rooms."""
        self.current_level += 1
        self.__generate_rooms()

    def display_rooms(self):
        """Output rooms to console."""
        for i in range(len(self.rooms)):
            print(f"Room {i}", end="\t")
        print()
    
    def enter_room(self, room_num):
        """
        Call the correct interaction function based on the object in the room.

        Params:
        room_num : int - Index of the selected room.

        Returns: 
        boolean - True if player survives interaction otherwise False.
        """
        room = self.rooms[room_num]
        print(room)
        room_obj = room.get_object()
        if isinstance(room_obj, Character):
            return self.__player_fight_character(room_obj)
        elif isinstance(room_obj, Item):
            self.__player_item_pickup(room_obj)
            return True
        
    def __player_fight_character(self, character):
        """
        Determine outcome when a player fights an enemy character.
        
        Returns:
        bool - True if player survives iteraction otherwise False."""
        while True:
                self.__player.apply_damage(character)
                if character.current_health <= 0:
                    print("The player has been victorius")
                    return True
                character.apply_damage(self.__player)
                if self.__player.current_health <= 0:
                    print("The player has died :(")
                    return False
                
    def __player_item_pickup(self, item):
        """Apply item effect to player."""
        item.apply_effect(self.__player)
