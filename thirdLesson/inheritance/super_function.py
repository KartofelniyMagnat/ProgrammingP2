class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, uni):
        super().__init__(name)
        self.uni = uni

s = Student("Ilya", "KBTU")
print(s.name, s.uni)