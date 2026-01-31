a = int(input())
nums = []
x = 0

while True:
    p = 2 ** x
    if p <= a:
        nums.append(str(p))
    else:
        break
    x += 1

print(" ".join(nums))
