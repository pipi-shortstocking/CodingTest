import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
ans = []

prefix = [0] * (n + 1) # 구간합을 저장할 배열
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + numbers[i - 1]

for i in range(m):
    i, j = map(int, input().split())
    ans.append(prefix[j] - prefix[i - 1])

for a in ans:
    print(a)