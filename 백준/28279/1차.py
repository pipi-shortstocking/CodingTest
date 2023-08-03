import sys
from collections import deque
input = sys.stdin.readline

arr = deque([])

n = int(input())
for _ in range(n):
    cmd = input().split()

    if cmd[0] == '1':
        arr.appendleft(cmd[1])
    elif cmd[0] == '2':
        arr.append(cmd[1])
    elif cmd[0] == '3':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif cmd[0] == '4':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif cmd[0] == '5':
        print(len(arr))
    elif cmd[0] == '6':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == '7':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif cmd[0] == '8':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])