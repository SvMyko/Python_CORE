contacts = {}

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

# додавання нового контакту
@input_error
def add_contact(name, phone):
    print(f"Adding contact: {name} - {phone}")
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} has been added"

# зміна номеру телефону існуючого контакту
@input_error
def change_phone(name, phone):
    print(f"Changing phone number for {name} to {phone}")
    contacts[name] = phone
    return f"Phone number for {name} has been updated to {phone}"

# отримання номера телефону контакту
@input_error
def get_phone(name):
    return f"The phone number for {name} is {contacts[name]}"

# виведення всіх контактів
def show_all():
    if not contacts:
        return "There are no contacts saved"
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    print("How can I help you?")
    while True:
        user_input = input().lower()
        if user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            try:
                name, phone = user_input.split()
                name = name.strip()
                phone = phone.strip()
                print(add_contact(name, phone))  # дотати контакт
            except ValueError:
                print("Please enter name and phone number separated by a space")
        elif user_input.startswith("change"):
            try:
                name, phone = user_input.split()
                name = name.strip()
                phone = phone.strip()  #
                print(change_phone(name, phone))  # змінити номре телефону
            except ValueError:
                print("Please enter name and phone number separated by a space")
        elif user_input.startswith("phone"):
            try:
                name = user_input.split()[1]
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
