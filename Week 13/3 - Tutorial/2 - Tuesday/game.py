class Character:

    def __init__(self, max_health, damage):
        self.max_health = max_health
        self.current_health = self.max_health
        self.damage = damage

    def take_damage(self, value):
        self.current_health -= value

    def apply_damage(self, other):
        print(f"{self} is applying damage to {other}.")
        other.take_damage(self.damage)


class Player(Character):

    def __init__(self, max_health, damage):
        super().__init__(max_health, damage)

    def pick_up(self, item):
        item.apply_effect(self)

    def increase_max_health(self, value):
        self.max_health += value

    def add_health(self, value):
        if self.current_health + value > self.max_health:
            self.current_health = self.max_health
        else:
            self.current_health += value

    def display_stats(self):
        stats = f"Player Health: {self.current_health}/{self.max_health}\n"
        stats += f"Player Damage: {self.damage}"
        print(stats)

    def __str__(self):
        return "Player"


class Warrior(Player):

    def __init__(self):
        super().__init__(120, 10)
        self.armor = 10

    def take_damage(self, value):
        value -= (value*self.armor/100)
        super().take_damage(value)

    def display_stats(self):
        super().display_stats()
        print(f"Armor: {self.armor}")

class Archer(Player):

    def __init__(self):
        super().__init__(90, 10)
        self.ranged_damage = self.damage * (25/100)

    def apply_damage(self, other):
        other.take_damage(self.ranged_damage)
        super().apply_damage(other)

    def display_stats(self):
        super().display_stats()
        print(f"Ranged Damage: {self.ranged_damage}")


class Zombie(Character):

    def __init__(self):
        super().__init__(40, 5)
    
    def __str__(self):
        return "Zombie"
    
class Goblin(Character):

    def __init__(self):
        super().__init__(30, 7)
    
    def __str__(self):
        return "Goblin"
    

class Item:
    def apply_effect(self, other):
        pass

from random import randint, choice
class Health(Item):
    def apply_effect(self, other):
        other.add_health(randint(10, 15))
        print("Player has received health.")
    
    def __str__(self):
        return "Health item"

class HeartBox(Item):
    def apply_effect(self, other):
        other.increase_max_health(15)
        other.add_health(15)
        print("Player's max health has increased!")

    def __str__(self):
        return "Heart Box"
    

class Room:
    items = [Health, HeartBox]
    enemies = [Zombie, Goblin]

    def __init__(self):
        self.__obj = choice(self.items+self.enemies)()

    def get_object(self):
        return self.__obj
    
    def __str__(self) -> str:
        return f"This room contains a {self.__obj}"
    

class World:

    def __init__(self, max_level):
        self.max_level = max_level
        self.current_level = 0
        self.rooms = []

    def __generate_rooms(self):
        self.rooms = [Room() for _ in range(randint(1,5))]

    def next_level(self):
        self.current_level += 1
        self.__generate_rooms()

    def display_rooms(self):
        for i in range(len(self.rooms)):
            print(f"Room {i}", end="\t")
        print()
    
    def enter_room(self, player, room_num):
        room = self.rooms[room_num]
        print(room)
        room_obj = room.get_object()
        if isinstance(room_obj, Character):
            while True:
                player.apply_damage(room_obj)
                if room_obj.current_health <= 0:
                    print("The player has been victorius")
                    return player
                room_obj.apply_damage(player)
                if player.current_health <= 0:
                    print("The player has died :(")
                    return room_obj
        elif isinstance(room_obj, Item):
            room_obj.apply_effect(player)
            return player
                

def main():

    world = World(3)

    user_choice = input("Please select a class below:\n1. Warrior\n2. Archer\n:")
    if user_choice == "1":
        player = Warrior()
    elif user_choice == "2":
        player = Archer()


    while world.current_level < world.max_level:
        world.next_level()
        print("Please select a room to enter:")
        world.display_rooms()
        user_choice = int(input(":"))
        if world.enter_room(player, user_choice) != player:
            break
        player.display_stats()
    else:
        print("Well done! You have beat the game.")


if __name__ == "__main__":
    main()          
