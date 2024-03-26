import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

# 투 포인터
left = 0
right = n - 1
cnt = 0

while left < right:
    temp = arr[left] + arr[right]

    if temp == x:
        cnt += 1
        left += 1  # 다음 단계로 이동
    elif temp < x:  # temp가 x보다 작을 경우, left + 1로 값 증가
        left += 1
    elif temp > x:  # right - 1로 값 감소
        right -= 1

print(cnt)
