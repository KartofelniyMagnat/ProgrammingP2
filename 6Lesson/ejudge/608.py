n = int(input())
numbers = list(map(int, input().split()))

result = sorted(set(numbers))
print(*result)