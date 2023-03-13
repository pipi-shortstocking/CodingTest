arr = [[0] * 101 for _ in range(101)]
num = int(input())
width = 0

for _ in range(num):
    x, y = list(map(int, input().split()))

    for row in range(x, x+10):
        for col in range(y, y+10):
            arr[row][col] = 1

for i in arr:
    width += i.count(1)

print(width)
