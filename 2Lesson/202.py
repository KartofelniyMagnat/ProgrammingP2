a = int(input())
sum = 0
b=input()
nums = list(map(int, b.split()))
for i in nums:
    sum+=i
print(sum)