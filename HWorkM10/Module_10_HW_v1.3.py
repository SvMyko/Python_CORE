from collections import UserDict


# FIXME: edit prompts
NAME_PROMPT = "NAME_PROMPT"
PHONE_PROMPT = "PHONE_PROMPT"
NEW_PHONE_PROMPT = "NEW_PHONE_PROMPT "
STOP_CMD = "STOP_CMD"


class Field:
    value: str
    prompt: str

    # FIXME: add value validation, throw ValueError
    def __init__(self):
        try:
            self.value = self.ask_for_value()
        except ValueError: print("Value is incorrect")


    @classmethod
    def ask_for_value(cls):
        return input(cls.prompt)


class Name(Field):
    prompt = NAME_PROMPT


class Phone(Field):
    prompt = PHONE_PROMPT

    @classmethod
    def get_list(cls):
        phones = []

        while True:
            try:
                phones.append(cls())
            except ValueError:
                break

        return phones

    def update(self):
        self.value = input(NEW_PHONE_PROMPT)


class Record:
    def __init__(self, name, phones=None):
        self.name = name
        self.phones = phones or list()

    @staticmethod
    def add_contact(name, phone, address_book):
        if len(name.strip()) == 0 or len(phone.strip()) == 0:
            raise ValueError("Please enter both name and phone number")
        record = address_book.get(name.lower())
        if not record:
            record = Record(name)
            address_book.add_record(record)
        record.add_phone(phone)
        return f"Added phone {phone} for contact {name}"

    def add_phone(self, phone):
        self.phones.append(phone)

    def del_phone(self):
        phone_to_remove = Phone.ask_for_value()
        self.phones = [phone for phone in self.phones if phone.value != phone_to_remove]

    def edit_phone(self):
        phone_to_edit = Phone.ask_for_value()
        for phone in self.phones:
            if phone.value == phone_to_edit:
                phone.update()
                return


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.phone] = record


# FIXME
def main():
    address_book = AddressBook()
    # record_class = Record()

    print("How can I help you?")
    while True:
        user_input = Field()
        if user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            try:
                print("Enter name and phone number separated by a space")
                user_input = field_input.ask_for_value()
                name, phone = user_input.split()
                name = name.strip()
                phone = phone.strip()
                # Додаємо номер в книгу контактів
                address_book.update({name: phone})
                print(f"Name: {name}, Phone: {phone} added to Contact list")
            except ValueError:
                print("ERROR: please enter a command again")
        elif user_input.startswith("change"):
            try:
                print("Enter new enter name and phone number separated by a space")
                user_input = input()
                # name, phone = user_input.split()
                # name = name.strip()
                # phone = phone.strip()  #
                # change_phone = record_class.edit_phone(name, phone)
                # print()  # змінити номер телефону
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
