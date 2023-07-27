import sys
input = sys.stdin.readline

s = str(input().rstrip())
cnt = 0

for i in range(1,len(s)):
    if s[i] != s[0] and s[i] != s[i-1]:
        cnt += 1

print(cnt)