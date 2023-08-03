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
    # result += arr[0] + arr[1]

    # arr.popleft()
    # arr.popleft()
    for i in range(2):
        result += arr.popleft()

    arr.appendleft(result)

print(result)