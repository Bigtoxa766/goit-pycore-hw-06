from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
         self.validate(name)
         super().__init__(name)

    @staticmethod
    def validate(name):
         if not name.strip():
              raise ValueError('Required field')

class Phone(Field):
    
    def __init__(self, phone_number):
        self.validate(phone_number)
        super().__init__(phone_number)

    @staticmethod
    def validate(phone_number):
        if not re.match(r'^\d{10}$', phone_number):
             raise ValueError(f'Phone number {phone_number} is not valid.')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
         self.phones.append(phone)
         print(self.phones)

    def remove_phone(self, contact_phone):
        self.phones = [phone for phone in self.phones if phone != contact_phone]
        print(self.phones)

    def edit_phone(self, contact_phone, new_phone):
        for phone in range(len(self.phones)):
            if self.phones[phone] == contact_phone:
                self.phones[phone] = new_phone
            
        print(self.phones)

    def find_phone(self, contact_phone):
         matching = [phone for phone in self.phones if phone == contact_phone]
         print(matching)
                  
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        print(record)

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

