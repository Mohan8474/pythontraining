
class person:
    #instance attribute
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company
    #methods
    def greet(self):
        print(f"HI my name is {self.name} and my age is {self.age}")

    def hello(self):
        print(f"Hi hello How are you? I am working in {self.company}")

#object instantiation
Mohan = person("Mohan", 23, "Annalect")
Ramesh = person("Ramesh", 25, "HCL")

#accessing class methods
Mohan.greet()
Mohan.hello()

Ramesh.greet()
Ramesh.hello()

person.greet(Mohan)
person.hello(Mohan)


class car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)


c1 = car("Toyota", 2016)
c1.display()

