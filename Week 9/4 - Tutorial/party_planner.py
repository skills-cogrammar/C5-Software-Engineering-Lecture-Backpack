"""
Allow the user to create a list of freinds with their emails to invite
to a party.

Add names and email to a list/dictionary
Remove names
create invite
send invite

"""

def add_friend(friends_dict):
    while True:
        name = input("Please enter the name of your friend: ")
        email = input("Please enter the email of your friend: ")
        friends_dict.update({email : name})
        user_choice = input("Would you like to add another friend(y/n): ")
        if user_choice == "n":
            break


def remove_friend(friends_dict):
    if friends_dict:
        print("Please select a friend to remove below: ")
        print("\tName\t\tEmail")
        for i, (email, name) in enumerate(friends_dict.items(), 1):
            print(f"{i}\t{name}\t\t{email}")
        while True:
            user_option = input(": ")
            if user_option.isnumeric() and 0 < int(user_option) <= len(friends_dict):
                emails = list(friends_dict.keys())
                friend_email = emails[int(user_option)-1]
                del friends_dict[friend_email]
                break
            print("Invalid selection!")
    else:
        print("No friend in list!")


def create_invite():

    date = input("Please enter the date for your party: ")
    location = input("Please enter the location for your party: ")
    rsvp = input("Please enter the RSVP date for your party: ")
    user_name = input("Please enter your name to sign at the end of the invite: ")

    invite = """Hi {name},
    
I would like to invite you to my birthday party on {date}.
The party will take place at {location}.
Please RSVP before {rsvp}.

Hope to see you there!
{user_name}"""

    return invite.format(name="{name}", date=date, location=location, 
                            rsvp=rsvp, user_name=user_name)


def send_invites(friends_dict, invite):
    user_email = input("Please enter your email: ")
    for email, name in friends_dict.items():
        email_str = f"From:\t{user_email}\n"
        email_str += f"To:\t{email}\n"
        email_str += "-"*80
        email_str += "\nSubject: Birthday Party Invite\n"
        email_str += "-"*80 + "\n"
        email_str += invite.format(name=name)
        with open(name+".txt", "w") as file:
            file.write(email_str)


def main():
    MENU = """Please select an option below:
    1. Add Friend to List
    2. Remove Friend from List
    3. Create Invite
    4. Send Invites

    0. Quit
    : """

    friends = {"james@gmail.com":"James", "peter@yahoomail.com" : "Peter"}
    print(friends.items())
    invite = ""

    while True:
        print("~~~~~~~~~~~~~Party Planner~~~~~~~~~~~~~")
        user_option = input(MENU)
        if user_option == "1":
            add_friend(friends)
        elif user_option == "2":
            remove_friend(friends)
        elif user_option == "3":
            invite = create_invite()
        elif user_option == "4":
            send_invites(friends, invite)
        elif user_option == "0":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()