import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[n - 1]
second = arr[n - 2]

sum = 0

while True:
    for i in range(k):  # k번씩만 더하기
        if m == 0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1

print(sum)
