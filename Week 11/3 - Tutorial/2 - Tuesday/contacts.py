from tabulate import tabulate


class Contact:

    def __init__(self, name, email="", cell_number=""):
        self.name = name
        self.email = email
        self.cell_number = cell_number

    def display_data(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nCell: {self.cell_number}")


class ContactList:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, index):
        del self.contacts[index]

    def display_contacts(self):
        headers = ["", "Name", "Email", "Cell"]
        data = []
        for i, contact in enumerate(self.contacts, 1):
            data.append([i, contact.name, contact.email, contact.cell_number])
        print(tabulate(data, headers=headers))

    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name)

    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.email},{contact.cell_number}\n")

    def retrieve_contacts(self):
        with open("contacts.txt", "r") as file:
            for line in file:
                name, email, cell_number = line.strip().split(",")
                self.add_contact(Contact(name, email, cell_number))


# my_contacts = ContactList()
# my_contacts.retrieve_contacts()
# my_contacts.display_contacts()
# my_contacts.add_contact(Contact("James", "j@gmail.com", "56150051"))
# my_contacts.add_contact(Contact("Adrian", "j@gmail.com", "56150051"))
# my_contacts.add_contact(Contact("Carl", "j@gmail.com", "56150051"))
# my_contacts.save_contacts()
# my_contacts.display_contacts()
# print()
# my_contacts.sort_contacts()
# my_contacts.display_contacts()
# my_contacts.contacts[0].display_data()
# my_contacts.remove_contact(0)
# print(my_contacts.contacts)





