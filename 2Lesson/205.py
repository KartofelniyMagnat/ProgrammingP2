a = int(input())

x = 0
while True:
    p = 2 ** x
    if p == a:
        print("YES")
        break
    elif p > a:
        print("NO")
        break
    x += 1