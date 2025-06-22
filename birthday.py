from collections import UserDict

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

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

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
    
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value==phone_number:
                self.phones.remove(phone)
                return True
        return False
    def edit_phone(self, old_phone_number, new_phone_number):
        for inx, phone in enumerate(self.phones):
            if phone.value==old_phone_number:
                self.phones[inx]==Phone(new_phone_number)
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
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")



        
          

