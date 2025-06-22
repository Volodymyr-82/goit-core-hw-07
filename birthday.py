from collections import UserDict
import re
from datetime import datetime 

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if not value.isdigit() or len(value)!=10:
            raise ValueError('Phone number must consist')
        super().__init__(value)

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value]=record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False
    
    def __str__(self):
        if not self.data:
            return "Адресна книга порожня"
        return "\n".join(str(record) for record in self.data.values())

class Record:
    def __init__(self, name):
        self.name=Name(name)
        self.phones=[]
        self.birthday = None
    
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_birthday(self, day):
        self.birthday=Birthday(day)


    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value==phone_number:
                self.phones.remove(phone)
                return True
        return False
    
    def edit_phone(self, old_phone_number, new_phone_number):
        for inx, phone in enumerate(self.phones):
            if phone.value==old_phone_number:
                self.phones[inx]=Phone(new_phone_number)
            return
        raise ValueError ('old number not found')
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value==phone_number:
                return phone
        return None
    
    def __str__(self):
            
        phone_str= "; ".join(phone.value for phone in self.phones)
        return f'Contact name: {self.name.value}, phones: {phone_str}'

            


class Birthday(Field):
    def __init__(self, value):
        data_format="%d.%m.%Y"
        try:
            datetime.strptime(value, data_format)
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("12.12.2024")
# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
    
        

