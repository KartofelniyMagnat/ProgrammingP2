a = input()
d = input()
nums = list(map(int, d.split()))
desc = list(map(int, a.split()))
res = []
sorting = []
begin = desc[1]
end = desc[2]
for i in range(len(nums)):
    if i < begin:
        res.append(nums[i])
    if i == begin:
        sorting.append(nums[i])
    if i == end:
        break
sorting.sort(reverse=True)
res += sorting  
print(*res)
