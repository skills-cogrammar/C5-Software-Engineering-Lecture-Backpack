class Character:
    """
    Base class for all character objects.
    
    Attributes:
    max_health : float - maximum health a player can have.
    current_health : float - Current health a character has.
    damage : flaot - The amount of damage a character can apply.
    """
    def __init__(self, max_health, damage):
        self.max_health = max_health
        self.current_health = self.max_health
        self.damage = damage

    def take_damage(self, value):
        """Subtracts incomming damage from health."""
        self.current_health -= value

    def apply_damage(self, other):
        """Applies damage value to given object."""
        print(f"{self} is applying damage to {other}.")
        other.take_damage(self.damage)


class Player(Character):
    """Base Class for all player objects."""
    def __init__(self, max_health, damage):
        super().__init__(max_health, damage)

    def pick_up(self, item):
        """Applies effect of item."""
        item.apply_effect(self)

    def increase_max_health(self, value):
        """Increases max health of player by given value."""
        self.max_health += value

    def add_health(self, value):
        """
        Increases health of player with given value. If the value
        exceeds the max_health attribute the players health will be
        set to the value of max_health.
        """
        if self.current_health + value > self.max_health:
            self.current_health = self.max_health
        else:
            self.current_health += value

    def display_stats(self):
        """Display all stats of player."""
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
        """Subtract incoming damage from health.
        Damage will be reduced by percentage of armor available."""
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
        """Apply ranged damage to given object then apply normal damage."""
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
