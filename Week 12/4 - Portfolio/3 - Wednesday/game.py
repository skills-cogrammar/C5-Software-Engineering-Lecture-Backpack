import os

class Item:

    def __init__(self, value) -> None:
        self.value = value
        self.x = 0
        self.y = 0


class Coin(Item):

    def __init__(self):
        super().__init__(50)


class Gem(Item):

    def __init__(self) -> None:
        super().__init__(100)


class Player:

    def __init__(self) -> None:
        self.score = 0
        self.x = 0
        self.y = 0

    def pick_up(self, item):
        self.score += item.value

    def update_coordinates(self, x=None, y=None):
        if x : self.x = x
        if y : self.y = y

    def get_player_coords(self):
        return (self.x, self.y)
    
    def __str__(self):
        return "P"

class World:

    def __init__(self, map_size):
        self.map = [["." for _ in range(map_size)] for _ in range(map_size)]
        self.player = None

    def set_player(self, player):
        self.player = player

    def move_player(self, direction):
        movements = {"w": (0, -1), "s": (0, 1), "a":(-1, 0), "d":(1,0)}
        player_coords = self.player.get_player_coords() 
        self.map[player_coords[1]][player_coords[0]] = "."
        player_coords = tuple(map(lambda x, y:#(0, 1)       (0, 0) result=(0, 1)
                             x+y, movements[direction], player_coords))
        self.player.update_coordinates(player_coords[0], player_coords[1])
        self.plot_object(self.player)
        

    def plot_object(self, obj):
        self.map[obj.y][obj.x] = obj

    def display_map(self):
        os.system('cls')
        for y in self.map:
            for x in y:
                print(x, end="")
            print()


world = World(5)
player = Player()

world.set_player(player)
world.plot_object(player)
world.move_player("s")
world.display_map()


item = Coin()
print(player.score)
player.pick_up(item)
player.pick_up(Gem())
print(player.score)


