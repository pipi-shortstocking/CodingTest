import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    num = sum(map(int, str(i))) + i
    if num == n:
        print(i)
        break
    if i == n:
        print(0)
        break
