import sys

input = sys.stdin.readline

s = int(input())
cnt = 0

for i in range(1, s):
    s -= i
    if s == 0:
        break
    if s < 0:
        s += i
        continue
    cnt += 1

print(cnt)
