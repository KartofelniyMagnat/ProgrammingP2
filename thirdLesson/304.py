class StringHandler:
    def __init__(self):
        self.gstring = ""
    def getString(self, a):
        self.gstring = a
    def printString(self):
        print(self.gstring.upper())
a = StringHandler()
b = input()
a.getString(b)
a.printString()


