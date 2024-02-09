# user = "user"

# def get_all_routines(user):
#     with open(f"{user}/routines.txt", 'r') as file:
#         return file.readlines()

# def print_list(lst):
#     for i, item in enumerate(lst,1):
#         print(i, item.strip(), sep=". ")

# routines = get_all_routines(user)
# print_list(routines)

# def get_routine(user, routine_name):
#     with open(f"{user}/routines/{routine_name}.txt", 'r') as routine:
#         return routine.readlines()


# def view_routine(program):
#     output = ("-"*80) + "\n"
#     for line in program:
#         split_line = line.strip().split(",")
#         output += (f"Exercise: {split_line[0]}\n"
#                     + f"Sets: {split_line[1]}\nReps: {split_line[2]}\n"
#                     + ("-"*80) + "\n")
#     print(output)

# routine = []
# user="user" 
# current_user, file_name = ""

# print("Please select one of your programs:")
# programs = get_all_routines(user)
# print_list(programs)
# input()
# selected_program = get_routine(user, "Shoulders")
# view_routine(selected_program)

# exercises = ["Shoulder Press", "Lateral Raise", "Push-ups", "Bench Press", "Leg Raises"]
# def choose_weight_exercise():
#     print("Please pick an exercise to add to your routine:")
#     print_list(exercises)
#     user_choice = int(input()-1)
#     return exercises[user_choice]

# exercises = ["Sprinting", "Jogging"]
# def choose_running_exercise():
#     print("Please pick an exercise to add to your routine:")
#     print_list(exercises)
#     user_choice = int(input()-1)
#     return exercises[user_choice]

# # Show HOF
# def create_exercise(choose_exercise):
#     exercise = choose_exercise()
#     sets = input("Please enter the amount of sets you would like to have:")
#     reps = input("Please enter the amount of reps would you like in each set:")
#     return [exercise, sets, reps]

# routine.append(create_exercise(choose_weight_exercise))
# routine.append(create_exercise(choose_running_exercise))

# def store_exercises(user, file_name, routine):
#     with open(f"{user}/programs/{file_name}.txt", "w") as file:
#         for exercise in routine:
#             line = f"{exercise[0]},{exercise[1]},{exercise[2]}\n"
#             file.write(line)

# store_exercises(current_user, file_name, routine)




# my_print = input
# my_print("Hello world!")

# input()


def run(**args):
    print(type(args))
# 
print(("Hello", "world", "!"))
for i in ("Hello", "world", "!"):
    print(i, end=" ")

x, y = (5, 6)