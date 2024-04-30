from contacts_processing import *
from addressbook import *

def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("There is no command in line!")
            break
        except UnboundLocalError:
            print("There is no command in line! Bye!")
            break

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "add-birthday":
            print(add_birth(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "birthday":
            print(show_birthday(args))
        elif command == "all":
            print(show_all())
        elif command == "congrats":
            print(congrats())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()