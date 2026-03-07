a = int(input())
b = input()
nums = list(map(int, b.split()))
res = []
mx = nums[0]
mn = nums[0]

for i in nums:
    if i > mx:
        mx = i
    if i < mn:
        mn = i

for i in nums:
    if i == mx:
        res.append(mn)
    else:
        res.append(i)

print(" ".join(map(str, res)))