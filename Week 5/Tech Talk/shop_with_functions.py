def add_item(shopping_list):
    """Add items to shopping list."""
    new_item = input("Please enter the name of the item you would like to add:")
    shopping_list.append(new_item)


def view_items(shopping_list):
    """View items in shopping list."""
    for i, item in enumerate(shopping_list, 1):
            print(i, item)

def delete_item(shopping_list):
    """Delete item from shopping list."""
    for i, item in enumerate(shopping_list, 1):
        print(i, item)
        index = input("Please enter the index of the item you would like to remove:\n")
        index = int(index)-1
        item = shopping_list[index]
        shopping_list.pop(index)
        print(f'{item} removed!')

def sort_items(shopping_list):
    """Sort shopping list."""
    shopping_list.sort()
    print("List sorted!")


def main():
    shopping_list = []

    while True:
        # Ask user to select an option form the menu
        menu = input("Please select an option below:\n1: Add item\n2: View List"\
                    "\n3: Delete item\n4: Sort List\n0: Exit\n")
        if menu == "1":
            add_item(shopping_list)
        elif menu == "2":
            view_items(shopping_list)
        elif menu == "3":
            delete_item(shopping_list)
        elif menu == "4":
            sort_items(shopping_list)
        elif menu == "0":
            # Exit program
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
    