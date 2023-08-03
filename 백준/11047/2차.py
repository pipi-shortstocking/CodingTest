import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
    a = int(input())
    coins.append(a)

for i in reversed(range(n)):
    print(i)
    cnt += k//coins[i]
    k = k % coins[i]

print(cnt)