class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def created(cls):
        return cls.count

a = Counter()
b = Counter()
print(Counter.created())