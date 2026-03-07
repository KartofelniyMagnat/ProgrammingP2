height = int(input())
width = int(input())

array = []
for _ in range(height):
    row = input().split()
    if len(row) == 1 and width > 1 and len(row[0]) == width:
        row = list(row[0])
    array.append(row)
sand = [0] * width
for i in range(height):
    for j in range(width):
        if array[i][j] == '0':
            sand[j] += 1
changed = True
while changed:
    changed = False
    for i in range(width):
        # first: take from the right neighbor
        if i + 1 < width and sand[i + 1] - sand[i] > 1:
            sand[i] += 1
            sand[i + 1] -= 1
            changed = True
        # then: take from the left neighbor
        if i - 1 >= 0 and sand[i - 1] - sand[i] > 1:
            sand[i] += 1
            sand[i - 1] -= 1
            changed = True
for i in range(height):
    for j in range(width):
        array[i][j] = '-'
for j in range(width):
    sj = sand[j]
    for i in range(height - 1, height - sj - 1, -1):
        array[i][j] = '0'
for i in range(height):
    print(*array[i])