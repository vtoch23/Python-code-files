class Person:
    def __init__(self, name: str):
        space = name.find(" ")
        fName = name[0:space]
        lName = name[space+1:]
        self.name = fName,lName
 
    def return_first_name(self):
        return self.name[0]  
    def return_last_name(self):
        return self.name[1]       
 
 
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())
 
    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name()) 