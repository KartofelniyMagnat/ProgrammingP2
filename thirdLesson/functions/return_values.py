def divmod_custom(a, b):
    q = a // b
    r = a % b
    return q, r

q, r = divmod_custom(17, 5)
print(q, r)