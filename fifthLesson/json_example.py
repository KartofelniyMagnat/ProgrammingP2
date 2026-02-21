"""
Python has a built-in package called json, which can be used to work with JSON data.
If you have a JSON string, you can parse it by using the json.loads() method.
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


"""
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(x["age"])