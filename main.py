from contacts_processing import load_data, parse_input, save_data, add_contact, change_contact, add_birth
from addressbook import OutputTerminal

def main():
    print("Welcome to the assistant bot!")
    book = load_data()
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
            save_data(book)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "add-birthday":
            print(add_birth(args, book))
        elif command == "phone":
            print(OutputTerminal.show_phone(OutputTerminal, args, book))
        elif command == "birthday":
            print(OutputTerminal.show_birthday(OutputTerminal, args, book))
        elif command == "all":
            print(OutputTerminal.show_all(OutputTerminal, book))
        elif command == "congrats":
            print(OutputTerminal.congrats(OutputTerminal, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()