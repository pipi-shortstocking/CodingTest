# 파이썬에는 스택이 따로 주어지지 않음
import sys

input = sys.stdin.readline

stack = []

n = int(input())
for i in range(n):
    # cmd, num = map(str, input().rstrip().split())
    cmd = str(input().rstrip())
    if cmd[:4] == "push":
        stack.append(cmd[5:])
    elif cmd == "pop":
        if stack:  # 비어있지 않을 경우
            print(stack[len(stack) - 1])
            # stack = stack[:len(stack)-1]
            del stack[len(stack) - 1]
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if not stack:  # 비어있을 경우
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if stack:
            print(stack[len(stack) - 1])
        else:
            print(-1)
