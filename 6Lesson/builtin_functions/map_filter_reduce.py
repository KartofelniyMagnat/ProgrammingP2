from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]


squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)

value = "123"
print("Type of value:", type(value))
print("Is value a string?", isinstance(value, str))


converted_int = int(value)
converted_float = float(value)
converted_str = str(converted_int)

print("Converted to int:", converted_int)
print("Converted to float:", converted_float)
print("Converted back to string:", converted_str)