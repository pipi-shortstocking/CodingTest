x, y, z = map(int, input().split())

via = [[[0 for _ in range(z)] for _ in range(y)] for _ in range(x)]
box = [[]]

for i in range(x):
    for j in range(y):
        box[i].append(list(map(int, input().split())))
    print(box)
