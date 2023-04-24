class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

person1 = Person("John", 30)
print(person1.get_name())
print(person1.get_age())
