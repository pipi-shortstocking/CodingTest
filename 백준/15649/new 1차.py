import sys
from itertools import permutations

input = sys.stdin.readline

n,m = map(int, input().split())

numbers = [i for i in range(1, n+1)]
per_arr = [p for p in permutations(numbers, m)]

for per in per_arr:
    print(" ".join(map(str, per))) # tuple인 per을 str로 변환

# 백트래킹 문제에서 백트래킹으로 해결 X