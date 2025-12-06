import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    brackets = input().strip()
    stack = []
    valid = True

    for ch in brackets:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                valid = False
                break
            stack.pop()

    if valid and not stack:
        print("YES")
    else:
        print("NO")