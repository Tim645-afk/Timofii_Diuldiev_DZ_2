

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"({self.name}, {self.age})"

    def __str__(self):
        return f"name: {self.name}, age: {self.age},"

    def get_birthday_year(self):
        return 2025 - self.age

Sigma = Person(name='Sigma', age=13)
Tim = Person(name='Tim', age=14)

print(Sigma)
print(Tim)

persons = [Sigma ,Tim ]

print(persons)

Tim_birthday = Tim.get_birthday_year()
print(Tim_birthday)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def diagonal(self):
        return (self.length ** 2 + self.width ** 2) ** 0.5

    def __str__(self):
        return f"Rectangle({self.length} x {self.width})"

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"



