import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

num = [0] * 2000001  # 해당 부분을 max(arr)+1로 할 경우, 잠재적인 오류의 가능성이 있음
cnt = 0

for i in arr:
    if num[x - i] == 1:
        cnt += 1
    num[i] = 1

print(cnt)
