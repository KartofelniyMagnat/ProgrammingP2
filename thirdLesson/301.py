def valid(n):
    g = ""
    for i in range(len(n)):
        if int(n[i]) %2 != 0:
            g = "Not valid"
            break
        else:
            g = "Valid"
    print(g)
a = input()
valid(a)