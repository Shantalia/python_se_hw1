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