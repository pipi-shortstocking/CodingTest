import sys
input = sys.stdin.readline

s = str(input().rstrip())

# print(s.count('0'))
# print(s.count('1'))

cnt = 0

# if s.count('0') == len(s) or s.count('1') == len(s):
#     print(0)

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

if cnt >= 2:
    print(int(cnt/2))
else:
    print(cnt)