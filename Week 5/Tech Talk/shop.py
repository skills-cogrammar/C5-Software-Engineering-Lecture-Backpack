shopping_list = []

while True:
    # Ask user to select an option form the menu
    menu = input("Please select an option below:\n1: Add item\n2: View List"\
                 "\n3: Delete item\n4: Sort List\n0: Exit\n")

    if menu == "1":
        # Ask user to enter an item and add the item to shopping list
        new_item = input("Please enter the name of the item you would like to add:")
        shopping_list.append(new_item)

    elif menu == "2":
        # View all items in shopping list
        for i, item in enumerate(shopping_list, 1):
            print(i, item)

    elif menu == "3":
        # Ask user to choose an index of an item to remove and remove item
        for i, item in enumerate(shopping_list, 1):
            print(i, item)
        index = input("Please enter the index of the item you would like to remove:\n")
        index = int(index)-1
        item = shopping_list[index]
        shopping_list.pop(index)
        print(f'{item} removed!')

    elif menu == "4":
        # Sort shopping list
        shopping_list.sort()
        print("List sorted!")

    elif menu == "0":
        # Exit program
        print("Goodbye!")
        break

    

    