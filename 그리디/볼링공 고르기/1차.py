import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
k = list(map(int, input().split()))

data = list(combinations(k, 2))
# print(data)
# print(len(data))
cnt = len(data)

for i in data:
    if i[0] == i[1]:
        cnt -= 1

print(cnt)
