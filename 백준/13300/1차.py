import sys

input = sys.stdin.readline

n, k = map(int, input().split())
stu = [[0, 0] for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())
    stu[y - 1][s] += 1

print(stu)
