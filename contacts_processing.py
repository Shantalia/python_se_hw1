from addressbook import Record, AddressBook
import pickle
from input_error import input_error

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

# функція обробки введеного рядка
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# функція додавання контакту в файл
@input_error
def add_contact(args, book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

# функція зміни існуючого контакту
@input_error
def change_contact(args, book):
    name, new_phone = args
    for nm in book.data:
        if nm == name:
            book.data[name].edit_phone(new_phone)
            return "Contact changed."
        elif nm != name:
            continue
        else:
            return "No contact with this name!"

# функція додавання др контакту
@input_error
def add_birth(args, book):
    name, birthday = args
    for nm in book.data:
        if nm == name:
            book.data[name].add_birthday(birthday)
            return "Birthday added."
        elif nm != name:
            continue
        else:
            return "No contact with this name!"