"""
Allow the user to create a list of friends with their emails to invite
to a party.

Add names and email to a list/dictionary
Remove names
create invite
send invite

"""
def add_friend(friends_dict):
    name = input("Please enter your friend's name:")
    email = input("Please enter your friend's email:")
    friends_dict.update({email:name})


def display_friends(friends_dict):
    print("Please select a former friend to remove below: ")
    print("\tName\t\tEmail")
    for i, (email, name) in enumerate(friends_dict.items(), 1):
        print(f"{i}\t{name}\t\t{email}")


def remove_friend(friends_dict):
    display_friends(friends_dict)
    while True:
        user_option = input(": ")
        if user_option.isnumeric() and 0 < int(user_option) <= len(friends_dict):
            friend_email = list(friends_dict.keys())[int(user_option)-1]
            del friends_dict[friend_email]
            break


def create_invite():

    date = input("Please enter the date for your birthday party: ")
    location = input("Please enter the location for your birthday party: ")
    rsvp = input("Please enter the RSVP date for your birthday party: ")
    user_name = input("Please enter your name to sign the invite with: ")

    invite = """Hi {name},
    
    I would like to invite you to my birthday party on {date}.
    The party will take place at {location}.
    Please RSVP before {rsvp}.
    
    Hope to see you there!
    {user_name}"""

    return invite.format(name="{name}", date=date, location=location, rsvp=rsvp, user_name=user_name)


def send_invites(friends_dict, invite):
    user_email = input("Please enter your email adress: ")
    for email, name in friends_dict.items():
        email_str = f"From:\t{user_email}\n"
        email_str += f"To:\t{email}\n\n"
        email_str += ("-"*80)
        email_str += "\nSubject: Birthday Party\n"
        email_str += ("-"*80) + "\n"
        email_str += invite.format(name=name)
        with open(name+".txt", "w") as file:
            file.write(email_str)
    print("Invites sent successfully!")


def main():
    MENU = """Please select an option below:

    1. Add Friend to List
    2. Remove Friend from List
    3. Create Invite
    4. Send Invites
    5. Display Friends

    0. Quit\n:"""

    friends = {"James@gmail.com": "James", "Dave@yahoo.com": "Dave"}
    invite = ""

    while True:
        print("~~~~~~~~~~~~Party Planner~~~~~~~~~~~~")
        user_option = input(MENU)
        if user_option == "1":
            add_friend(friends)
        elif user_option == "2":
            remove_friend(friends)
        elif user_option == "3":
            invite = create_invite()
        elif user_option == "4":
            if invite:
                send_invites(friends, invite)
            else:
                print("No invite!")
        elif user_option == "5":
            display_friends(friends)


if __name__ == "__main__":
    main()