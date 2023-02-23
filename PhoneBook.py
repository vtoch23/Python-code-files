class PhoneBook:
    def __init__(self):
        self.__persons = {}
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name, number, personAddress = None)
            if len(number) > 0:
                self.__persons[name].add_number(number)  
        else:
            if len(number) > 0:
                self.__persons[name].add_number(number)
    def add_address(self, name, address):
        if not name in self.__persons:
            self.__persons[name] = Person(name, address)
            if len(address) > 0:
                self.__persons[name].add_address(address) 
        else:
            if len(address) > 0:
                self.__persons[name].add_address(address)
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        else:
            return self.__persons[name].personName, self.__persons[name].numbersList, self.__persons[name].personAddress
    def all_entries(self):
        return self.__persons
class Person:
    def __init__(self, personName: str, number = None, personAddress = None):
        self.personName = personName
        self.numbersList = []
        self.personAddress = personAddress
    def add_number(self, number):
        self.numbersList.append(number)
    def add_address(self, address):
        self.personAddress = address
    def name(self):
        return self.personName
    def numbers(self):
        return self.numbersList
    def address(self):
        if self.personAddress != "":
            return self.personAddress
        else:    
            return None
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
    def help(self):
        print("commands: ")
        print("0 to exit, 1: add entry, 2: search entries, 3: add address")
    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)     
    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        if numbers:
            if numbers[1]:
                for number in numbers[1]:
                    print(number)    
            else:
                print("number unknown")
            if numbers[2]:
                print(numbers[2])
                
            else:
                print("address unknown") 
                return 
                
        else:
            print("number unknown")
            print("address unknown")
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()  
            else:
                self.help()  
application = PhoneBookApplication()
application.execute()