import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
min = 300000

for arr in combinations(card, 3):
    sum = arr[0] + arr[1] + arr[2]
    if sum > m:
        continue
    elif (m-sum) < min:
        min = m-sum
        result = sum

print(result)
