import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

n = int(input())
for _ in range(n):
    cmd = input().rstrip().split()

    if cmd[0] == "push_front":
        queue.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        queue.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
            # print(queue.popleft())
    elif cmd[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])
            queue.pop()
            # print(queue.pop())
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])
