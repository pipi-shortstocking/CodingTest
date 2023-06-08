import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

# print()
# 산술 평균
print(round(sum(arr) / n))

# 중앙값
arr.sort()
print(arr[n // 2])

# 최빈값
count = Counter(arr).most_common()
# print(count)
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

# 범위
print(arr[n - 1] - arr[0])
