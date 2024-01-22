import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cnt = (m // (k + 1)) * k + m % (k + 1)

first = arr[n - 1]
second = arr[n - 2]

sum = first * cnt + second * (m - cnt)

print(sum)
