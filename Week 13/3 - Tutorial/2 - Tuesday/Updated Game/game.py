from world import World

def main():

    world = World(3)

    user_choice = input("Please select a class below:\n1. Warrior\n2. Archer\n:")
    if user_choice == "1":
        world.set_player("w")
    elif user_choice == "2":
        world.set_player("a")

    while world.current_level < world.max_level:
        world.next_level()
        print("Please select a room to enter:")
        world.display_rooms()
        user_choice = int(input(":"))
        if not world.enter_room(user_choice):
            break
        world.get_player().display_stats()
    else:
        print("Well done! You have beat the game.")


if __name__ == "__main__":
    main()          
