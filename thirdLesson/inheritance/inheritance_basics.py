class Animal:
    def eat(self):
        print("Eating...")

class Cat(Animal):
    def meow(self):
        print("Meow!")

c = Cat()
c.eat()
c.meow()