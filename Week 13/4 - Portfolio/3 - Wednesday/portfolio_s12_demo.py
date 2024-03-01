import random

class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        raise NotImplementedError("Subclasses must implement the introduce method.")

    def interact(self, choice):
        raise NotImplementedError("Subclasses must implement the interact method.")

class Hero(Character):
    def introduce(self):
        return f"I am the valiant hero, {self.name}. Ready to embark on an epic adventure!"

    def interact(self, choice):
        if choice == 'fight':
            return f"{self.name} bravely fights against evil!"
        elif choice == 'talk':
            return f"{self.name} negotiates for peace and understanding."
        else:
            return f"{self.name} chooses a different path."

class Villain(Character):
    def introduce(self):
        return f"I am the cunning villain, {self.name}. Prepare for chaos and destruction!"

    def interact(self, choice):
        if choice == 'fight':
            return f"{self.name} unleashes chaos and engages in a fierce battle!"
        elif choice == 'talk':
            return f"{self.name} manipulates and deceives to achieve their sinister goals."
        else:
            return f"{self.name} takes an unexpected turn, surprising everyone."

# Storybook
def interactive_story():
    hero_name = input("Enter the name of your hero: ")
    villain_name = input("Enter the name of the villain: ")

    hero = Hero(hero_name)
    villain = Villain(villain_name)

    print(hero.introduce())
    print(villain.introduce())

    user_choice = input("What should the hero do? (fight/talk): ").lower()

    hero_outcome = hero.interact(user_choice)
    villain_outcome = villain.interact(random.choice(['fight', 'talk']))

    print("\nOutcome:")
    print(f"Hero: {hero_outcome}")
    print(f"Villain: {villain_outcome}")

if __name__ == "__main__":
    interactive_story()
