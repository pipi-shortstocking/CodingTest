import sys

input = sys.stdin.readline

s = str(input().rstrip())
now = 1

for i in s:
    if int(i) == 0:
        continue
    else:
        now *= int(i)

print(now)
