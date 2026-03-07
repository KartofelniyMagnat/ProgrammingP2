from math import ceil
from math import floor
a = input()
b = list(map(str, a.split()))
if b[2] == "+":
    print(f"{int(b[0])+int(b[1])}")
elif b[2] == "-":
    print(f"{int(b[0])-int(b[1])}")
elif b[2] == "*":
    print(f"{int(b[0])*int(b[1])}")
elif b[2] == "/":
    if b[1] == "0":
        print("Doesn't exist")
    else:
        print(f"{floor(float(int(b[0])/int(b[1])))}")

