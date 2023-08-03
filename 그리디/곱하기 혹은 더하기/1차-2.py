import sys

input = sys.stdin.readline

s = str(input().rstrip())

now = int(s[0])

for i in range(1, len(s)):
    if int(s[i]) <= 1 or now <= 1:
        now += int(s[i])
    else:
        now = now * int(s[i])

print(now)
