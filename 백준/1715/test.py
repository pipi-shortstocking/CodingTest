import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
result = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort()
arr = deque(arr)

while len(arr) >= 2:
    temp1 = arr.popleft()
    temp2 = arr.popleft()
    result += temp1 + temp2

    arr.appendleft(temp1+temp2)
    print(arr)

print(result)

# 해당 답이 오답처리되는 이유 :
# arr는 지속적으로 sort 되어야 최선의 값이 도출됨