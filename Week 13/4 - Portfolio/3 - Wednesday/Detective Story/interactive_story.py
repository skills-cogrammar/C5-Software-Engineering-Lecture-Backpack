import random

class Detective:
    def __init__(self, name, intro_file):
        self.name = name
        self.intro_file = intro_file

    def introduce(self):
        with open(self.intro_file, 'r') as file:
            return file.read().strip()

    def investigate(self, choice):
        outcome_file = f"{self.name}_{choice}.txt"
        with open(outcome_file, 'r') as file:
            return file.read().strip()

class MysteryStory:
    def __init__(self, detectives_file, plot_points_file):
        self.detectives = {}
        self.plot_points = []
        self.load_detectives(detectives_file)
        self.load_plot_points(plot_points_file)

    def load_detectives(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            detective_name, intro_file = line.strip().split(',')
            self.detectives[detective_name] = Detective(detective_name, intro_file)

    def load_plot_points(self, file_path):
        with open(file_path, 'r') as file:
            self.plot_points = [line.strip() for line in file.readlines()]

    def run_story(self):
        detective_name = input("Enter the name of your detective: ")
        crime_scene = input("Enter the location of the crime scene: ")

        detective = self.detectives.get(detective_name, Detective(detective_name, "default_intro.txt"))

        print(detective.introduce())
        print(f"\nYou arrive at the crime scene in {crime_scene}.")

        for plot_point in self.plot_points:
            print(f"\nPlot: {plot_point}")
            user_choice = input("What should the detective do? (examine/question): ").lower()

            detective_outcome = detective.investigate(user_choice)
            print("\nOutcome:")
            print(f"{detective_outcome}")

if __name__ == "__main__":
    mystery_story = MysteryStory("detectives.txt", "plot_points_mystery.txt")
    mystery_story.run_story()
