a = int(input())
b = input()
nums = list(map(str, b.split()))
dict = {}
freq = 0
res = []
for i in nums:
    dict[i] = dict.get(i,0) + 1
for key, val in dict.items():
    if val > 1:
        freq+=val
print(a-freq)
