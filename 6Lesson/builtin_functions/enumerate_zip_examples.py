names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

print("Using enumerate():")
for index, name in enumerate(names, start=1):
    print(index, name)

print()
print("Using zip():")
for name, score in zip(names, scores):
    print(name, score)

print()

numbers_as_strings = ["1", "2", "3"]
numbers_as_ints = [int(x) for x in numbers_as_strings]

for s, n in zip(numbers_as_strings, numbers_as_ints):
    print(f"String: {s}, Integer: {n}, Type: {type(n)}")