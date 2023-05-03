import sys
input = sys.stdin.readline

arr = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))

# for i in range(n):
#     arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
arr.sort()

for i in range(n):
    print(arr[i][1], arr[i][0])
