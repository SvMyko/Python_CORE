from collections import UserDict

# декоратор обробки помилок
def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "This contact does not exist"
        except ValueError:
            return "Please enter name and phone number separated by a space"
        except IndexError:
            return "Please enter a contact name"
    return inner


class Field:
    def __init__(self,value):
        self.value = value

class Name:
    def __init__(self, name):
        self.name = name

class Phone:
    def __init__(self, phone):
        self.phone = phone

class AddressBook(UserDict):
    

class Record(Name, Phone):
    def __init__(self, name, phone):
        super().__init__(name)
        super().__init__(phone)
    #додавання контакту
    def add_record(self,name, phone):
        address_book = AddressBook()
        address_book.update({name: phone})
        return f"Contact {self.name} with phone number {self.phone} has been added"
    # зміна номеру телефону існуючого контакту
    def change_phone(self,name, phone):
        print(f"Changing phone number for {name} to {phone}")
        contacts[name] = phone
        return f"Phone number for {name} has been updated to {phone}"
    # зміна номеру телефону існуючого контакту
    def change_phone(self, name, phone):
        print(f"Changing phone number for {name} to {phone}")
        contacts[name] = phone
        return f"Phone number for {name} has been updated to {phone}"



# отримання номера телефону контакту
@input_error
def get_phone(name):
    return f"The phone number for {name} is {contacts[name]}"

# виведення всіх контактів
def show_all():
    if not AddressBook():
        return "There are no contacts saved"
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in list.address_book()])

def main():

    print("How can I help you?")
    while True:
        user_input = input().lower()
        if user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            try:
                print("Enter name and phone number separated by a space")
                user_input = input()
                name, phone = user_input.split()
                name = name.strip()
                phone = phone.strip()
                # передаємо значення в класи Name та Phone
                name_obj = Name(name)
                phone_obj = Phone(phone)
                address_book = AddressBook()
                print(f"Name: {name_obj.name}, Phone: {phone_obj.phone}")
            except ValueError:
                print("ERROR: please enter a command again")
        elif user_input.startswith("change"):
            try:
                print("Enter new enter name and phone number separated by a space")
                user_input = input()
                name, phone = user_input.split()
                name = name.strip()
                phone = phone.strip()  #
                change_phone = AddressBook.change_phone(name, phone)
                print()  # змінити номер телефону
            except ValueError:
                print(f"Name: {AddressBook.name}, Phone: {AddressBook.phone}")
        elif user_input.startswith("phone"):
            try:
                print("Enter name ")
                user_input = input()
                name = user_input
                print(get_phone(name))  # вивести номер
            except IndexError:
                print("Please enter a name")
        elif user_input == "show all":
            print(show_all())  # виветси всі контакти
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("I do not understand, please try again")


if __name__ == "__main__":
    main()
