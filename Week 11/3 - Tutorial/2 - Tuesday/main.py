"""
Create contact list manager

contact
- name
- email
- cell number


Add contacts
remove contacts
view contacts
sort contacts

contacts should be saved to textfile 
and retrieved when starting program"""
from contacts import ContactList, Contact


def create_contact():
    name = input("Please enter the name of your contact: ")
    email = input(f"Please enter {name}'s email address: ")
    cell_number = input(f"Please enter {name}'s cell number: ")
    return Contact(name, email, cell_number)


def main():

    MENU = """Contact Manager
    
1. Display Contacts
2. Add Contact
3. Remove Contact
4. Sort Contacts

0. Quit
"""

    contact_list = ContactList()

    contact_list.retrieve_contacts()

    while True:
        user_option = input(MENU)

        if user_option == "1":
            contact_list.display_contacts()
        elif user_option == "2":
            new_contact = create_contact()
            contact_list.add_contact(new_contact)
        elif user_option == "3":
            contact_list.display_contacts()
            while True:
                user_index = input("Please choose a contact to delete: ")
                if user_index.isdigit() and 0 < int(user_index) <= len(contact_list.contacts):
                    user_index = int(user_index)
                    break
            contact_list.remove_contact(user_index-1)
        elif user_option == "4":
            contact_list.sort_contacts()
            print("Contacts have been sorted.")

        elif user_option == "0":
            contact_list.save_contacts()
            break
            



if __name__ == "__main__":
    main()
