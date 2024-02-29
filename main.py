from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class NameException(Exception):
    pass


class Name(Field):
    def make_name(self, name):
        if name is None:
            raise NameException(f"There isn't name. Please, enter name!\n")
        else:
            return Name(name)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError
        elif not value.isdigit():
            raise ValueError
        else:
            super().__init__(value)


class Record:
    def __init__(self, name=None):
        try:
            self.name = Name.make_name(self, name)

        except NameException as e:
            print(e)

        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        for number in self.phones:
            if str(number) == phone:
                self.phones.remove(number)

    def edit_phone(self, *args, **kwargs):
        if args[0] in (p.value for p in self.phones):
            try:
                for number in self.phones:
                    if str(number) == args[0]:
                        ind = self.phones.index(number)
                        self.phones[ind] = Phone(args[1])
            except ValueError as e:
                print(e)
        else:
            raise ValueError

    def find_phone(self, phone):
        try:
            for number in self.phones:
                if str(number) == str(Phone(phone)):
                    return number
        except PhoneException as e:
            print(e)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, find_name):
        if self.data.get(find_name):
            our_name = self.data.get(find_name)
            return our_name
        else:
            return None

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
        else:
            print(f"=>Name {name} isn't exists")


