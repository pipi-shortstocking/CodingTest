import sys
input = sys.stdin.readline

n = int(input())
money = []

for _ in range(n):
    arr = list(map(int, input().split()))
    last = []
    cnt = 0

    if arr[0] == arr[1]:
        cnt += 1
        last.append(arr[0])
    if arr[1] == arr[2]:
        cnt += 1
        last.append(arr[1])
    if arr[2] == arr[0]:
        cnt += 1
        last.append(arr[2])
    
    if cnt == 3:
        money.append(10000 + arr[0] * 1000)
    elif cnt == 1:
        money.append(1000 + arr[0] * 100)
    else:
        money.append(max(arr) * 100)

print(max(money))