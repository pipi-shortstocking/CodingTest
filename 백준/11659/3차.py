import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp = 0
sum = [0]

for a in arr:
    temp += a
    sum.append(temp)

for a in range(m):
    i, j = map(int, input().split())
    print(sum[j]-sum[i-1])
