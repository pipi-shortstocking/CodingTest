import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    brackets = list(input().strip())
    stack = []

    while brackets:
        if brackets[0] == '(':
            stack.append(brackets[0])
            del brackets[0]
        elif brackets[0] == ')' and stack:
            stack.pop()
            del brackets[0]
        elif brackets[0] == ')' and not stack:
            break

    if brackets or stack:
        print("NO")
    else:
        print("YES")