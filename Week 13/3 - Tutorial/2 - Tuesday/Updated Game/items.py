from random import randint

class Item:
    """Abstract class representing an item a player can pick up."""
    def apply_effect(self, other):
        """Apply the effect attached to item."""
        pass

class Health(Item):
    """Applies health to player upon pick up."""
    def apply_effect(self, other):
        other.add_health(randint(10, 15))
        print("Player has received health.")
    
    def __str__(self):
        return "Health item"

class HeartBox(Item):
    """Increases maximum and current health of teh player upon pick up."""
    def apply_effect(self, other):
        other.increase_max_health(15)
        other.add_health(15)
        print("Player's max health has increased!")

    def __str__(self):
        return "Heart Box"
