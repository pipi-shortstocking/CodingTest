import sys

input = sys.stdin.readline

s = str(input().rstrip())
arr = []

for i in range(len(s)):
    arr.append(s[i:])

arr.sort()

for line in arr:
    print(line)
