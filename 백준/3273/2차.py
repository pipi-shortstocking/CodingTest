import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

num = [0] * (max(arr) + 1)

cnt = 0
for j in arr:
    if num[x - j] == 1:
        cnt += 1
    num[j] += 1

print(cnt)
