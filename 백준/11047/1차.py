import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
    a = int(input())
    coins.append(a)

while(k!=0):
    for i in range(len(coins)):
        if coins[i] > k:
            num = int(k//coins[i-1])
            cnt += num
            k -= coins[i-1]*num

print(cnt)