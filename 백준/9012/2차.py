import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    string = str(input().rstrip())
    cnt = 0

    for i in string:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break

    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")

# 하지만 본 문제는 스택 활용 문제!