import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = sum(arr)
result -= max(arr)

# 직접 반복문을 돌리는 것이 시간이 더 오래 걸림
# result = 0
# arr.sort()

# for i in range(n-1):
#     result += arr[i]

print(result)
