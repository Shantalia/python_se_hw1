from collections import UserDict
from datetime import datetime, timedelta
from abc import abstractmethod, ABC
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

# декоратор для обробки помилки ValueError
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:   
            return "Give me correct name/phone/birthday please."  
        except IndexError:
            return "There is no result. Give me name/phone/birthday please."
    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('Phone is incorrect')
        
class Birthday(Field):
    def __init__(self, value):
        try:
            bithrday_day = datetime.strptime(value, "%d.%m.%Y").date()
            bithrday_day = bithrday_day.strftime("%d.%m.%Y")
            super().__init__(bithrday_day)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.birthday = None
    
    def add_phone(self, phone): 
        self.phone = Phone(phone)

    def edit_phone(self, new_phone): 
        self.phone.value = new_phone
            
    def add_birthday(self, birthday):
            self.birthday = Birthday(birthday)

    def __str__(self):
        return f"------------\nContact name: {self.name.value}\nPhone: {self.phone.value}\nBirthday: {self.birthday}"

class AddressBook(UserDict):
    def add_record(self, obj_rec): 
        self.data[obj_rec.name.value] = obj_rec

    def find(self, name): 
        for nm in self.data:
            if nm == name:
                return self.data[name].phone.value
            elif nm != name:
                continue
            else:
                return "No such contact!"
            
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        delta = today + timedelta(days=7)
        future_year = today + timedelta(days=365)
        for user in self.data:
            if self.data[user].birthday:
                birth_day = datetime.strptime(self.data[user].birthday.value, "%d.%m.%Y").date()
                if ((birth_day.day < today.day) and (birth_day.month <= today.month)) or \
                    ((birth_day.day > today.day) and (birth_day.month < today.month)):
                    congratulation_date = datetime(year = future_year.year, month = birth_day.month, day = birth_day.day)
                else:
                    congratulation_date = datetime(year = today.year, month = birth_day.month, day = birth_day.day)
                    day_of_week = congratulation_date.weekday()
                    if (congratulation_date.date() <= delta):
                        if day_of_week >= 5:
                            congratulation_date = datetime(year = today.year, month = birth_day.month, day = birth_day.day+(7-day_of_week))
                        print(f'{user} : {str(congratulation_date.date())}')
            else:
                continue
        return "-----------------"    

class OutputVariants(ABC):
    @abstractmethod
    def show_phone(self):
        pass

    @abstractmethod
    def show_all(self):
        pass

    @abstractmethod
    def show_birthday(self):
        pass

    @abstractmethod
    @input_error
    def congrats(self):
        pass

class OutputTerminal(OutputVariants):
    # функція виведення існуючого контакту по імені
    @input_error
    def show_phone(self, args, book):
        self.name = args[0]
        return book.find(self.name)
    
    # функція виведення всіх контактів
    @input_error
    def show_all(self, book):
        for key, record in book.data.items():
            print(record)
        return "--------------" 
    
    # функція виведення ДР контакту по імені
    @input_error
    def show_birthday(self, args, book): 
        self.name = args[0]
        for nm in book.data:
            if (nm == self.name) and (book.data[self.name].birthday):
                return book.data[self.name].birthday.value
            elif nm != self.name:
                continue
            else:
                return "No contact with this name or no added birthday!"
    
    # функція виведення всіх контактів з ДР на цьому тижні
    @input_error  
    def congrats(self, book): 
        return book.get_upcoming_birthdays()
