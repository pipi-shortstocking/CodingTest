import sys
input = sys.stdin.readline

n = int(input()) # 우유 가게의 수
store = list(map(int,input().split()))

order = [0,1,2]

cnt = 0

for i in range(n):
    for j in range(3):
        if store[i] == order[j]:
            cnt += 1

print(cnt)