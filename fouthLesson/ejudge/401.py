def generator(n):
    i = 0
    a = 1
    if n == 0:
        pass
    elif n == 1:
        print(0)
    while i <= n+1:
        yield i
        i, a = a, i+a

a = int(input())
print(",".join(map(str, generator(a))))