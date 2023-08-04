import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    string = str(input().rstrip())
    stack = []

    for ps in string:
        if ps == "(":
            stack.append(ps)
        elif ps == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:           
            print("YES")