import sys
input = sys.stdin.readline

n,x = map(int, input().split())

a = list(map(int, input().split()))

arr = []

for num in a:
    if num < x:
        arr.append(num)

print(*arr)