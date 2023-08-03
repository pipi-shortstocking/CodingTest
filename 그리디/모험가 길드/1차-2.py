import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
result = 0

arr.sort()  # 오름차순

for i in arr:
    cnt += 1  # 그룹에 들어간 수 (자신 포함)
    if cnt >= i:  # 그룹에 들어간 수가 현재 값보다 크면
        result += 1
        cnt = 0

print(result)
