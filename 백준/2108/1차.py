import sys

input = sys.stdin.readline

n = int(input())
arr = []
count = {}

for _ in range(n):
    # num = int(input())
    # arr.append(num)
    arr.append(int(input()))

# print()
# 산술 평균
print(round(sum(arr) / n))

# 중앙값
arr.sort()
print(arr[n // 2])

# 최빈값
for i in arr:
    count[i] = arr.count(i)

# print(sorted(count.items(), key=lambda x: x[1]))
# print(len(count))

max_arr = []
appear = max(count.values())

for key, value in count.items():
    if value == appear:
        max_arr.append(key)
max_arr.sort()

if len(max_arr) > 1:
    print(max_arr[1])
else:
    print(max_arr[0])

# rev_count = dict(map(reversed, count.items()))
# print(rev_count)

# 범위
# print(max(arr) - min(arr))
print(arr[n - 1] - arr[0])
