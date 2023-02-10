n = int(input())
plans = input().split()

move = ['L', 'R', 'U', 'D']
nx = [0, 0, -1, 1]
ny = [-1, 1, 0, 0]

x, y = 1, 1

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            px = x + nx[i]
            py = y + ny[i]
    if px < 1 or px > n or py < 1 or py > n:
        continue
    x, y = px, py

print(x, y)
