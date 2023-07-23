import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        arr.append(cmd[1])
    elif cmd[0] == "pop":
        if arr:
            print(arr[0])
            arr.popleft()
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if arr:
            print(arr[len(arr) - 1])
        else:
            print(-1)
