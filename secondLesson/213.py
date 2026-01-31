a = int(input())
counter = 0
for i in range(2,a+1):
    if a % i == 0:
        counter +=1
if counter > 1 or a < 2:
    print("No")
else:
    print("Yes")