from birthday import AddressBook, Record
def input_error(parse_input):
    def inner(*args, **kwargs):
        try:
            return parse_input(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

@input_error
def parse_input(user_input):
    parts=user_input.strip().split()
    cmd = parts[0].lower()
    args=parts[1:]
    return cmd, args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


def change_contact(args, book):
    name, phone = args
    book[name] = phone
    return "Contact updated."

def show_phone(args, book):
    try:
        name= args[0]
        num=book[name]
        return num
    except KeyError:
        return f"Contact '{name}' not found."

def show_all(book):
    
    return book 

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    record.add_birthday(birthday)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    return f"{name}'s birthday: {record.birthday.value}"

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    result = "Upcoming birthdays:\n"
    for birthday_info in upcoming:
        result += f"{birthday_info['name']}: {birthday_info['birthday']}\n"
    return result.strip()


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()