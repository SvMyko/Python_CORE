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
    value: str


    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    def update(self, value):
        self.value = value

@input_error
class Record:
    def __init__(self, name, phones=None):
        self.name = name
        self.phones = phones or list()

    def __str__(self):
        return ", ".join(p.value for p in self.phones)

    def add_phone(self, phone):
        self.phones.append(phone)

    def del_phone(self):
        phone_to_remove = Phone.ask_for_value()
        self.phones = [phone for phone in self.phones if phone.value != phone_to_remove]

    def edit_phone(self, current_phone, new_phone):
        for phone in self.phones:
            if phone.value == current_phone:
                phone.value = new_phone
                return
        return ValueError

@input_error
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all(self):
        return self.data.values()

    def get_phone(self, name):
        return self.data.get(name)

    def __str__(self):
        return  "\n".join(f"{name}: {record}" for name, record in self.data.items())


def main():
    address_book = AddressBook()

    print("How can I help you?")
    while True:
        user_input = input().lower()
        if user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            try:
                user_input = input("Enter name and phone number separated by a space: ")
                name, *phones = user_input.split()
                name = Name(name)
                phones = [Phone(p) for p in phones]
                record = Record(name, phones)
                # Додаємо номер в книгу контактів
                address_book.add_record(record)
                print(f"Name: {name}, Phone: {record} added to Contact list")
            except ValueError:
                print("ERROR: please enter a command again")

        elif user_input.startswith("change"):
            try:
                name = input("Enter name: ")
                record = address_book.get_phone(name)
                if not record:
                    print('Contact doesnt exist')
                    continue
                current_phone = input("Enter curent phone number: ")
                new_phone = input("Enter new phone number: ")
                # Змінюємо номер
                record.edit_phone(current_phone, new_phone)
                print(f"Name: {name}, Phone: {current_phone} changed to {new_phone}")
            except ValueError:
                print(f"Name: {AddressBook.name}, Phone: {AddressBook.phone}")

        elif user_input.startswith("phone"):
            try:
                name = input("Enter a contact name: ")
                record = address_book.get_phone(name)
                print(f"Name: {name}, Phone(s):  {record}")
            except IndexError:
                print("Please enter a name")

        elif user_input == "show all":
            print(f'List of contacts: {address_book}')  # виветси всі контакти
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("I do not understand, please try again")



if __name__ == "__main__":
    main()
