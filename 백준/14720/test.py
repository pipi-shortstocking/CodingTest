import sys
input = sys.stdin.readline

n = int(input()) # 우유 가게의 수
store = list(map(int,input().split()))
order = 0
cnt = 0

for i in range(n):
    if store[i] == 0 and order == 0:
        cnt += 1
        order = 1
    elif store[i] == 1 and order == 1:
        cnt += 1
        order = 2
    elif store[i] == 2 and order == 2:
        cnt += 1
        order = 0

print(cnt)