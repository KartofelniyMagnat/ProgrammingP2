class Bird:
    def sound(self):
        return "..."

class Parrot(Bird):
    def sound(self):          # override
        return "Hello!"

p = Parrot()
print(p.sound())