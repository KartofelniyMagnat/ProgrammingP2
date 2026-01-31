a = int(input())
sum = 0

b=input()
nums = list(map(int, b.split()))
for i in nums:
    if i > 0:
        sum+=1
print(sum)