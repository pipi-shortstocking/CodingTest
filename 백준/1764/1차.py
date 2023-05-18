import sys

input = sys.stdin.readline

n, m = map(int, input().split())
listen = []
see = []

for i in range(n):
    listen.append(str(input().rstrip()))

for j in range(m):
    see.append(str(input().rstrip()))

arr = list(set(listen) & set(see))  # 합집합
arr.sort()

print(len(arr))
for name in arr:
    print(name)
