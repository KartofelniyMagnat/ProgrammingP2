a = int(input())
b = input()
nums = list(map(int, b.split()))
for i in range(len(nums)):
    nums[i] = nums[i] * nums[i]
print(*nums)