import sys

input = sys.stdin.readline

n = int(input())

i = 1
cnt = 0
while i * i <= n:
    i += 1
    cnt += 1

print(cnt)
